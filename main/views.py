from django.shortcuts import render, redirect
from .models import CandidForm, candidate
from django.contrib.auth import logout as authout, login as auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from .choices import EVENT_OPTIONS, CERTIFICATE_OPTIONS, CERTIFICATE_PATHS
from django.db.models import Q
from .resources import *
from tablib import Dataset
from django.http import HttpResponse
from reportlab.pdfgen import canvas
import os
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.core.validators import RegexValidator, EmailValidator
from django.utils.html import strip_tags
from django.core.exceptions import ValidationError
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import NameObject, DictionaryObject, FloatObject, createStringObject
from io import BytesIO
from .forms import UserRegisterForm

# Login view


def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, "Invalid Crendentials")
            return render(request, 'main/login.html')
    return render(request, 'main/login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return render(request, 'main/dashboard.html')
        else:
            # Extract form errors
            error_messages = []
            for field, errors in form.errors.items():
                for error in errors:
                    error_messages.append(f"{field.capitalize()}: {error}")

            # Combine all errors into a single message
            full_error_message = " ".join(error_messages)
            messages.error(request, full_error_message)
            
            return render(request, 'main/register.html', {'form': form})
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})
# Dashboard View


@login_required(redirect_field_name='login')
def dashboard(request, sent=0):
    if sent == 1:
        context = {'candidates': candidate.objects.filter(is_sent=True)}
    else:
        context = {'candidates': candidate.objects.filter(
            Q(is_sent=False))}

    return render(request, 'main/dashboard.html', context)


# add Candiate form
@login_required(redirect_field_name='login')
def addCandidate(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            email = request.POST['email']
            college = request.POST['college']
            event = request.POST['event1']
            certi_type = request.POST['Certificate1']
            candid = candidate(name=name, email=email, college=college,
                               certificate_type=certi_type, event=event)
            candid.save()
            return redirect('dashboard')
        except:
            messages.info('Email already exists')
    context = {'events': EVENT_OPTIONS, 'types': CERTIFICATE_OPTIONS}
    return render(request, 'main/candidateform.html', context)


@login_required(redirect_field_name='login')
def update_candidate(request, pk):
    candid = candidate.objects.filter(id=pk).first()
    if request.method == 'POST':
        try:
            print(candid)
            candid.name = request.POST['name']
            candid.college = request.POST['college']
            candid.event = request.POST['event1']
            candid.certificate_type = request.POST['Certificate1']
            candid.email = request.POST['email']
            candid.is_sent = False
            candid.save()
            return redirect('dashboard')
        except:
            messages.error(
                request, 'An error occurred while updating the candidate.')

    context = {
        'candidate': candid,

        'events': EVENT_OPTIONS,  # Make sure to define EVENT_OPTIONS in your context
        # Make sure to define CERTIFICATE_OPTIONS in your context
        'types': CERTIFICATE_OPTIONS
    }
    return render(request, 'main/candidateform.html', context)


@login_required(redirect_field_name='login')
def delete_candidate(request, email):
    candid = candidate.objects.filter(email=email).first()
    candid.delete()
    return redirect('dashboard')

# add csv file


@login_required(redirect_field_name='login')
def addcsv(request):
    if request.method == "POST":
        candidate_resource = CandidateResource()
        dataset = Dataset()
        new_candidate = request.FILES.get('document')
        if new_candidate is None:
            messages.info(request, 'No file selected')
            return render(request, 'main/csvform.html')
        imported_data = dataset.load(new_candidate.read(), format='xlsx')
        for data in imported_data:
            print(data)
            value = candidate(
                data[0],
                data[1],
                data[2],
                data[3],
                False,
                True,
                data[4],
                data[5],
            )
            value.save()
        messages.info(request, 'data has been added successfully')
    return render(request, 'main/csvform.html')

# logout view


@login_required(redirect_field_name='login')
def logout(request):
    authout(request)
    return redirect('login')


def add_text_to_pdf(input_path, name, college, event):
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=(2000, 2000))
    if (input_path[0][0] == 'CA_G' or input_path[0][0] == 'CA_P' or input_path[0][0] == 'CA_S' or input_path[0][0] == 'CA_Part'):
        can.setFontSize(22)
        can.drawString(550, 395, str(name))
        can.setFontSize(16)
        can.drawString(350, 358, str(college))
    elif(input_path[0][0] == 'BC2' or input_path[0][0] == 'BD2' or input_path[0][0] == 'BA1' or input_path[0][0] == 'BA2' or  input_path[0][0] == 'BV' or input_path[0][0] == 'BG'):
        can.setFontSize(19)
        can.drawString(420, 291, str(name))
        can.setFontSize(17)
        can.drawString(275, 263, str(college))
        can.setFontSize(19)
        can.drawString(345, 234, str(event))
    elif(input_path[0][0] == 'BA3'):
        can.setFontSize(19)
        can.drawString(420, 291, str(name))
        can.setFontSize(17)
        can.drawString(275, 263, str(college))
    else:
        can.setFontSize(22)
        can.drawString(550, 395, str(name))
        can.setFontSize(20)
        can.drawString(350, 358, str(college))
        can.setFontSize(22)
        can.drawString(475, 318, str(event))
    can.save()

    packet.seek(0)
    new_pdf = PyPDF2.PdfReader(packet)

    # read your existing PDF
    with open(input_path[0][1], 'rb') as pdf_file:

        existing_pdf = PyPDF2.PdfReader(pdf_file)
        page = existing_pdf.pages[0]
        output = PyPDF2.PdfWriter()

        page.merge_page(new_pdf.pages[0])
        output.add_page(page)

        # Create a byte stream to store the modified PDF content
        output_stream = BytesIO()
        output.write(output_stream)
        output_stream.seek(0)

        # Return the modified PDF content as a byte array
        return output_stream.getvalue()

# @login_required


@login_required(redirect_field_name='login')
def send_email(request, id):
    try:
        candid = candidate.objects.get(id=id)
    except candidate.DoesNotExist:
        candid = None
    if not candid or not candid.is_valid:
        return render(request, 'main/candidateform.html')
    context = {'candid': candid}
    name = candid.name
    competition = candid.event
    college = candid.college
    certi_type = candid.certificate_type
    input_path = list(filter(lambda x: x[0] == certi_type, CERTIFICATE_PATHS))
    print(certi_type)
    certificate_pdf = add_text_to_pdf(input_path, name, college, competition)
    email = EmailMessage(
        'Certificate of Achievement',
        f'Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!',
        'your@gmail.com',  # Replace with your email
        [candid.email],
    )
    email.attach(f'{candid.name + candid.email}_certificate.pdf',
                 certificate_pdf, 'application/pdf')
    email.send()
    candid.is_sent = True
    candid.save()
    context['email'] = candid.email
    print("hi")
    return redirect('dashboard')


@login_required(redirect_field_name='login')
def mail_all(request):
    candids = candidate.objects.filter(is_sent=False)[:50]
    count = 0
    for candid in candids:
        try:
            context = {'candid': candid}
            name = candid.name
            competition = candid.event
            college = candid.college
            certi_type = candid.certificate_type

            input_path = list(
                filter(lambda x: x[0] == certi_type, CERTIFICATE_PATHS))
            certificate_pdf = add_text_to_pdf(
                input_path, name, college, competition)
            email = EmailMessage(
                'Certificate of Achievement',
                f'Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!',
                'your@gmail.com',  # Replace with your email
                [candid.email],
            )
            email.attach(f'{candid.name + candid.email}_certificate.pdf',
                         certificate_pdf, 'application/pdf')
            email.send()
            candid.is_sent = True
            candid.save()
            count += 1
        except:
            messages.info(request, f'Not able to send email to {candid.email}')
    messages.info(request, f'Mail sent to {count}')
    return redirect('dashboard')
