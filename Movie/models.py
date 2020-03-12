from django.db import models

# Create your models here.
CHOICES = (
	('Action','action'),('Comedy',"comedy"),('Romance',"romance"),('Thriller',"thriller"),
	("Horror","Horror"))

class movie(models.Model):
	MovieID=models.CharField(max_length=50)
	MovieTitle=models.CharField(max_length=50)
	MovieYear=models.IntegerField()
	MovieGenre=models.CharField(max_length=100,choices=CHOICES,default="Comedy")

	def __str__(self):
		return self.MovieID + '-' + self.MovieTitle

class ratings(models.Model):
	UserId = models.IntegerField()
	MovieID = models.IntegerField()
	rating = models.IntegerField()
	review = models.TextField()

	def __str__(self):
		return self.review+'-by-'+ str(self.UserId)

class watched_List(models.Model):
	UserId = models.IntegerField()
	MovieTitle = models.CharField(max_length=111)

	def __str__(self):
		return self.MovieTitle
