from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Location


# Create your views here.

def home(request):
    message='Be  am beated'
    try:
        images=Image.get_images()

    except Exception as e:
        raise  404
    locations=Location.get_location()
    return render(request,"index.html",{'message':message,'images':images,'locations':locations})

def location(request,locate_id):

    try:
        locations=Location.get_location()
        images=Image.objects.filter(locate=locate_id)
    except Exception as e:
        raise 404

    return render(request,'location.html',{'images':images,'locations':locations})
