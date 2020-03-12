from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()
# settings.AUTH_USER_MODEL
from django_countries.fields import CountryField


CHOICES = (('18-30','18-30'),('31-41','31-41'),('42-55','42-55'),('55 above','55 above'))

g_CHOICES = (('male','male'),('female','female'))
genre_CHOICES  = (
	('Action','action'),('Comedy',"comedy"),('Romance',"romance"),('Thriller',"thriller"),
	("Horror","Horror"))


MF_CHOICES = (('Avid user','Avid user'),('Once in a week','Once in a week'),('few times in month','few times in month'))

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	hobbies = forms.CharField(max_length=100,help_text="use , for multiple entries")
	age_group = forms.ChoiceField(choices=CHOICES)
	gender = forms.ChoiceField(choices=g_CHOICES)
	country = CountryField().formfield()
	location = forms.CharField(max_length=30,)
	favorite_genre = forms.ChoiceField(choices=genre_CHOICES,)
	TypeOfUser = forms.ChoiceField(choices=MF_CHOICES,)
	

	class Meta:
		model = User
		fields = ['first_name','last_name','username','email',
		'password1','password2','hobbies','age_group','gender',
		'country','location','favorite_genre','TypeOfUser']


