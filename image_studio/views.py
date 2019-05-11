from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Location
import pyperclip

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

    '''
    copy and paste
    '''


    return render(request,'location.html',{'images':images,'locations':locations})

def search(request):
    if 'category' in request.GET and request.GET['category']:
        search_word=request.GET.get('category')
        search_images=Image.search_image(search_word)

        return render(request,"search.html",{"images":search_images})

    else:
        message="No image found"
        return render(request,"search.html",{"message":message})
