from django.db import models

# Create your models here.
class Movie(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now_add=True)


class Retailer(models.Model):
	name = models.CharField(max_length=100)
	movies = models.ManyToManyField(Movie, related_name='retailer')
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now_add=True)

class Price(models.Model):
	name = models.CharField(max_length=100)
	movies = models.ManyToManyField(Movie, related_name='price')
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now_add=True)
