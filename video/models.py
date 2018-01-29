from django.db import models

# Create your models here.

class Movie(models.Model):
	title = models.CharField(max_length=256)
	length = models.PositiveIntegerField()
	year = models.PositiveIntegerField()
	def __str__(self):
		return self.title

class Customer(models.Model):
	fname = models.CharField(max_length=256)
	lname = models.CharField(max_length=256)
	mobile = models.PositiveIntegerField()
	def __str__(self):
		return self.fname+' '+self.lname
