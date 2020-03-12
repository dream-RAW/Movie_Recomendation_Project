from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

CHOICES = (('18-30','18-30'),('31-41','31-41'),('42-55','42-55'),('55 above','55 above'))
g_CHOICES = (('male','male'),('female','female'))
genre_CHOICES  = (
    ('Action','action'),('Comedy',"comedy"),('Romance',"romance"),('Thriller',"thriller"),
    ("Horror","Horror"))

MF_CHOICES = (('Avid user','Avid user'),('Once in a week','Once in a week'),('few times in month','few times in month'))

class User(AbstractUser):
    hobbies = models.CharField(max_length=30, blank=True)
    age_group = models.CharField(max_length=100,choices=CHOICES,default="18-30")
    gender = models.CharField(max_length=100,choices=g_CHOICES,default="male")
    country = CountryField()
    location = models.CharField(max_length=30, blank=True)    
    favorite_genre = models.CharField(max_length=100,choices=genre_CHOICES,default="Comedy")
    TypeOfUser = models.CharField(max_length=100,choices=MF_CHOICES,default="few times in month")


