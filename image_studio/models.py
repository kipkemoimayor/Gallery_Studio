from django.db import models

# Create your models here.
class Image(models.Model):
    name=models.CharField(max_length=30)

class Location(models.Model):
    location=models.CharField(max_length=30)

class Category(models.Model):
    Category=models.CharField(max_length=30)
