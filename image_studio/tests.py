from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class LocationTest(TestCase):
    def setUp(self):
        self.collins=Location(location="Nairobi");

    def test_instance(self):
        self.assertTrue(isinstance(self.collins,Location))

    def test_initialization(self):
        self.assertTrue(self.collins.location,"Nairobi")

    def test_save_image(self):
        self.collins.save_location()
        location=Location.objects.all()
        self.assertTrue(len(location)>0)

    def test_delete(self):
        self.collins.delete_location()
        location=Location.objects.all()
        self.assertTrue(len(location)==0)

class TestCategory(TestCase):
    def setUp(self):
        self.category=Category(Category="love")

    def test_initialization(self):
        self.assertTrue(self.category.Category,"love")

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    def test_save_category(self):
        self.category.save_category()
        category=Category.objects.all()
        self.assertTrue(len(category)>0)


class ImageTest(TestCase):
        def setUp(self):

            self.collins=Location(location="Nairobi");
            self.collins.save_location()

            self.new_categ=Category(Category="food")
            self.new_categ.save_category()


            self.new_image=Image(name="blast",decription="sweet",image="",categ=self.new_categ,locate=self.collins)
            self.new_image.save()


        def test_save_image(self):
            self.new_image.save_image()
            saved=Image.objects.all()
            self.assertTrue(len(saved)>0)

        def test_delete_image(self):
            self.new_image.delete_image()
            saved=Image.objects.all()
            self.assertTrue(len(saved)==0)

        def test_test_image_id(self):
            self.new_image.get_id()
            id=Image.objects.all()
            self.assertTrue(len(id)>0)


        def TearDown(self):
            Location.objects.all().delete()
            Category.objects.all().delete()
            Image.objects.all().delete()
