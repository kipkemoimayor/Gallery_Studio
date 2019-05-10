from django.db import models

# Create your models here.

class Location(models.Model):
    location=models.CharField(max_length=30)

    def __str__(self):
        return self.location

class Category(models.Model):
    Category=models.CharField(max_length=30)

    def __str__(self):
        return self.Category

class Image(models.Model):
    name=models.CharField(max_length=30)
    decription=models.CharField(max_length=200)
    locate=models.ForeignKey(Location)
    categ=models.ForeignKey(Category)
    image=models.ImageField(upload_to='gallery/',blank=True)
    upload_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['name']
