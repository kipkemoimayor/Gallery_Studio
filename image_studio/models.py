from django.db import models

# Create your models here.

class Location(models.Model):
    location=models.CharField(max_length=30)

    def __str__(self):
        return self.location
    @classmethod
    def get_location(cls):
        locations=cls.objects.all()
        return locations

    '''
    saving location
    '''
    def save_location(self):
        self.save()

    def delete_location(self):
        location=Location.objects.all().delete()
        return location


class Category(models.Model):
    Category=models.CharField(max_length=30)

    def __str__(self):
        return self.Category

    @classmethod
    def search_image(cls,search_word):
        image=cls.objects.filter(Category__icontains=search_word)
        return image

    def save_category(self):
        self.save()


class Image(models.Model):
    name=models.CharField(max_length=30)
    decription=models.CharField(max_length=200)
    locate=models.ForeignKey(Location)
    categ=models.ForeignKey(Category)
    image=models.ImageField(upload_to='gallery/',blank=True)
    upload_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_images(cls):
        images=cls.objects.all()
        return images

    # @classmethod
    # def get_by_location(cls):
    #     images=cls.objects.filter(locate=1)
    #     return images



    class Meta:
        ordering=['name']

    '''
    saving images to database
    '''

    def save_image(self):
        self.save()


    #deleting image

    def delete_image(self):
        deleted=Image.objects.all().delete()
        return deleted
