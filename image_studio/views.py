from django.shortcuts import render
from django.http import HttpResponse
from .models import Image


# Create your views here.

def home(request):
    message='Be  am beated'
    images=Image.get_images()
    return render(request,"index.html",{'message':message,'images':images})
