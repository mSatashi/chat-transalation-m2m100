from django.db import models
import time
import random
# Create your models here.

class User(models.Model):

    lang_id = [
        ('af', 'Afrikaans'),
        ('am', 'Amharic'),
        ('ar', 'Arabic'),
        ('ast', 'Asturian'),
        ('az', 'Azerbaijani'),
        ('ba', 'Bashkir'),
        ('be', 'Belarusian'),
        ('bg', 'Bulgarian'),
        ('bn', 'Bengali'),
        ('br', 'Breton'),
        ('ca', 'Catalan'),
        ('ceb', 'Cebuano'),
        ('cs', 'Czech'),
        ('cy', 'Welsh'),
        ('da', 'Danish'),
        ('de', 'German'),
        ('el', 'Greek'),
        ('en', 'English'),
        ('es', 'Spanish'),
        ('et', 'Estonian'),
        ('fa', 'Persian'),
        ('ff', 'Fulah'),
        ('fi', 'Finnish'),
        ('fr', 'French'),
        ('fy', 'Western Frisian'),
        ('ga', 'Irish'),
        ('gd', 'Gaelic'),
        ('gl', 'Galician'),
        ('gu', 'Gujarati'),
        ('ha', 'Hausa'),
        ('he', 'Hebrew'),
        ('hi', 'Hindi'),
        ('hr', 'Croatian'),
        ('hu', 'Hungarian'),
        ('hy', 'Armenian'),
        ('id', 'Indonesian'),
        ('ig', 'Igbo'),
        ('ilo', 'Iloko'),
        ('is', 'Icelandic'),
        ('it', 'Japanese'),
        ('jv', 'Javanese'),
        ('ka', 'Georgian'),
        ('kk', 'Kazakh'),
        ('km', 'Central Khmer'),
        ('kn', 'Kannada'),
        ('ko', 'Korean'),
        ('lb', 'Luxembourgish'),
        ('lg', 'Ganda'),
        ('ln', 'Lingala'),
        ('lo', 'Lao'),
        ('lt', 'Lithuanian'),
        ('lv', 'Latvian'),
        ('mg', 'Malagasy'),
        ('mk', 'Macedonian'),
        ('ml', 'Malayalam'),
        ('mn', 'Mongolian'),
        ('mr', 'Marathi'),
        ('ms', 'Malay'),
        ('my', 'Burmese'),
        ('ne', 'Nepali'),
        ('nl', 'Dutch'),
        ('no', 'Norwegian'),
        ('ns', 'Northern Sotho'),
        ('oc', 'Occitan'),
        ('or', 'Oriya'),
        ('pa', 'Panjabi'),
        ('pl', 'Polish'),
        ('ps', 'Pushto'),
        ('pt', 'Portuguese'),
        ('ro', 'Romanian'),
        ('ru', 'Russian'),
        ('sd', 'Sindhi'),
        ('si', 'Sinhala'),
        ('sk', 'Slovak'),
        ('sl', 'Slovenian'),
        ('so', 'Somali'),
        ('sq', 'Albanian'),
        ('sr', 'Serbian'),
        ('ss', 'Swati'),
        ('su', 'Sundanese'),
        ('sv', 'Swedish'),
        ('sw', 'Swahili'),
        ('ta', 'Tamil'),
        ('th', 'Thai'),
        ('tl', 'Tagalog'),
        ('tn', 'Tswana'),
        ('tr', 'Turkish'),
        ('uk', 'Ukrainian'),
        ('ur', 'Urdu'),
        ('uz', 'Uzbek'),
        ('vi', 'Vietnamese'), 
        ('wo', 'Wolof'),
        ('xh', 'Xhosa'),
        ('yi', 'Yiddish'),
        ('yo', 'Yoruba'),
        ('zh', 'Chinese'),
        ('zu', 'Zulu'),

    ]

    random_id = random.randrange(100000000,int(time.time()))
    unique_id = models.IntegerField(default= random_id)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    mail = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    language = models.CharField(max_length=3, choices=lang_id, default=None)
    img = models.ImageField(upload_to='chatTranslation/uploads/images/users/', null=True)
    status = models.CharField(max_length=255)

    class Meta:
        db_table = "user"

    def __str__(self):
        return f'{self.fname} {self.lname}' 


class Message(models.Model):
    incoming_msg_id = models.IntegerField()
    outgoing_msg_id = models.IntegerField()
    msg = models.CharField(max_length=1000)
    translated_msg = models.CharField(max_length=1000)

    class Meta:
        db_table = "message"
        db_table_comment = "Chat and Translated Message"