from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Location


# Create your views here.

def home(request):
    message='Be  am beated'
    images=Image.get_images()
    locations=Location.get_location()
    return render(request,"index.html",{'message':message,'images':images,'locations':locations})

def location(request):
    images=Image.get_by_location()
    return render(request,'location.html',{'images':images})
