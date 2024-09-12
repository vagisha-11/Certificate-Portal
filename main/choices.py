# all the certificate choices and events choices stored as tuples
CERTIFICATE_OPTIONS = [
        ('CA_G', 'Campus Ambassador Gold'),
        ('CA_P', 'Campus Ambassador Platinum'),
        ('CA_S', 'Campus Ambassador Silver'),
        ('CA_Part', 'Campus Ambassador Participation'),
        ('P' , 'Participant' ),
        ('W' , 'Winner'),
        ('R1' , 'First Runner'),
        ('R2' , 'Second Runner'),
        ('R' , 'Runner'),
        ('SA' , 'Special Achievement'),
        ('MP', 'Manshakti Participant'),
        ('MW', 'Manshakti Winner'),
        ('BB', 'Best Bassist'),
        ('BC1', 'Best Choreographer'),
        ('BD1', 'Best Designer'),
        ('BM1', 'Best Model'),
        ('BM2', 'Best Makeup Artist'),
        ('BG', 'Best Guitarist'),
        ('BD2', 'Best Drummer'),
        ('BC2', 'Best Original Composser'),
        ('BA1', 'Best Actor'),
        ('BA2', 'Best Actoress'),
        ('BA3', 'Best Adjudicator'),
        ('BV', 'Best Vocalist'),
    ]
CERTIFICATE_PATHS = [
        ('CA_G', './certificates/CAGold.pdf'),
        ('CA_P', './certificates/CAPlatinum.pdf'),
        ('CA_S', './certificates/CASilver.pdf'),
        ('CA_Part','./certificates/CAParticipant.pdf' ),
        ('P' ,'./certificates/Participation.pdf'),
        ('W' ,'./certificates/Winner.pdf' ),
        ('R1' ,'./certificates/Runnerup.pdf' ),
        ('R2' ,'./certificates/SecondRunnerup.pdf'),
        ('R' , './certificates/Runnerup.pdf'),
        ('BB' , './certificates/Bestbassist.pdf'),
        ('BC1' , './certificates/Bestchoreo.pdf'),
        ('BD1' , './certificates/Bestdesigner.pdf'),
        ('BM1' , './certificates/Bestmodel.pdf'),
        ('BM2' , './certificates/Bestmakeup.pdf'),
        ('SA' , './certificates/Winner.pdf'),
        ('MP','./certificates/Winner.pdf'),
        ('MW','./certificates/Winner.pdf'),
        ('BG', './certificates/Bestguitar.pdf'),
        ('BD2', './certificates/Bestdrummer.pdf'),
        ('BC2', './certificates/Bestcomposer.pdf'),
        ('BA1', './certificates/Bestactor.pdf'),
        ('BA2', './certificates/Bestactress.pdf'),
        ('BA3', './certificates/PD.pdf'),
        ('BV', './certificates/Bestvocal.pdf'),
    ]

EMAIL_CONTENT = [
        ('CA_G', 'Dear {candid.name},\n\nPlease find the attached certificate for your achievement .\n\nCongratulations!'),
        ('CA_P', 'Dear {candid.name},\n\nPlease find the attached certificate for your achievement .\n\nCongratulations!'),
        ('CA_S', 'Dear {candid.name},\n\nPlease find the attached certificate for your achievement .\n\nCongratulations!'),
        ('P', 'Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!'),
        ('W', 'Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!'),
        ('R1', 'Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!'),
        ('R2', 'Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!'),
        ('R', 'Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!'),
        ('BB' , 'Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!'),
        ('BC' , 'Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!'),
        ('BD' , 'Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!'),
        ('BM1' , 'Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!'),
        ('BM2' , 'Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!'),
        ('SA' , 'Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!'),
        ('MP','Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!'),
        ('MW','Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!'),
        ('BG', 'Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!'),
        ('BD2', 'Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!'),
        ('BC2', 'Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!'),
        ('BA1', 'Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!'),
        ('BA2', 'Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!'),
        ('BA3', 'Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!'),
        ('BV', 'Dear {candid.name},\n\nPlease find the attached certificate for your achievement in {candid.event}.\n\nCongratulations!'),
        # ('SA' , ''),
        # ('MP',''),
        # ('MW',''),
    ]

EVENT_OPTIONS = [
        ('None', 'None'),
        ('Haute Couture', 'Haute Couture'),
        ('States of Dress', 'States of Dress'),
        ('Glamour Nova', 'Glamour Nova'),
        ('Rock-O-Phonix', 'Rock-O-Phonix'),
        ('Mr & Miss Alcheringa', 'Mr & Miss Alcheringa'),
        ('Crossfade', 'Crossfade'),
        ('Alcher Got Talent', 'Alcher Got Talent'),
        ('Rap Battle', 'Rap Battle'),
        ('Theatrix', 'Theatrix'),
        ('Monodrama', 'Monodrama'),
        ('Halla Bol', 'Halla Bol'),
        ('Electric Heels', 'Electric Heels'),
        ('Step Up', 'Step Up'),
        # ('Dancing Duo', 'Dancing Duo'),
        # ('So You Think You Can Dance', 'So You Think You Can Dance'),
        ('Short Cut', 'Short Cut'),
        ('Sixth String', 'Sixth String'),
        ('Navras', 'Navras'),
        ('Raga High', 'Raga High'),
        ('Unplugged', 'Unplugged'),
        ('Voice of Alcheringa', 'Voice of Alcheringa'),
        ('Choir', 'Choir'),
        ('Just A Minute', 'Just A Minute'),
        ('Mehfil - e - Alcheringa', 'Mehfil - e - Alcheringa'),
        ('Parliamentry Debate', 'Parliamentry Debate'),
        ('Poetry Slam - Hindi', 'Poetry Slam - Hindi'),
        ('Poetry Slam - English', 'Poetry Slam - English'),
        ('Zephyr', 'Zephyr'),
        ('Face Art', 'Face Art'),
        ('Ink The Tee', 'Ink The Tee'),
        ('Graffiti', 'Graffiti'),
        ('Clay Modelling', 'Clay Modelling'),
        ('Live Sketching', 'Live Sketching'),
        ('Rangoli', 'Rangoli'),
        ('Who is it?', 'Who is it?'),
        ('5 on 5 football', '5 on 5 football'),
        ('Arm Wrestling', 'Arm Wrestling'),
        ('3 on 3 Basketball', '3 on 3 Basketball'),
        ('Gully Cricket', 'Gully Cricket'),
        ('3 on 3 Volleyball', '3 on 3 Volleyball'),
        ("Director's Cut", "Director's Cut"),
        ('Musically', 'Musically'),
        ('Snap Thrillz', 'Snap Thrillz'),
        ('Custom Brush', 'Custom Brush'),
        ('Doodle Pad', 'Doodle Pad'),
        ('Alcher Diva/Hunk', 'Alcher Diva/Hunk'),
        ('Xpressions', 'Xpressions'),
        ('Parliamentry Debate', 'Parliamentry Debate'),
        ('General Quiz', 'General Quiz'),
        ('Business Quiz', 'Business Quiz'),
        ('Sports Quiz', 'Sports Quiz'),
        ('Entertainment Quiz', 'Entertainment Quiz'),
        ('Comic Quiz', 'Comic Quiz'),
        ('India Quiz', 'India Quiz'),
        ('Manshakti Poetry', 'Manshakti Poetry'),
        ('Manshakti Art', 'Manshakti Art'),
        ('Critical Damage', 'Critical Damage'),
        ('Just Reel It', 'Just Reel It'),
        ('Best out of Waste', 'Best out of Waste'),       
        ('Sixth String', 'Sixth String'),
]

