from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Location,Category
import pyperclip

# Create your views here.

def home(request):
    message='Be  am beated'
    try:
        images=Image.get_images()

    except Exception as e:
        raise  Http404()

    locations=Location.get_location()
    return render(request,"index.html",{'message':message,'images':images,'locations':locations})

def location(request,locate_id):

    try:
        locations=Location.get_location()
        images=Image.objects.filter(locate=locate_id)
    except Exception as e:
        raise Http404()
        assert False

    '''
    copy and paste
    '''


    return render(request,'location.html',{'images':images,'locations':locations})

def search(request):
    if 'Category' in request.GET and request.GET['Category']:
        search_word=request.GET.get('Category')
        search_images=Category.search_image(search_word)
        if len(search_images)>0:
            arr=[]
            for i in search_images:
                arr.append(i.id)

            category=arr[0]
            images=Image.objects.filter(categ_id=category)



            '''
            getting locations
            '''
            try:
                locations=Location.get_location()
            except ValueError:
                raise Http404()
                assert False



            return render(request,"search.html",{"images":images,'word':search_word,'categories':search_images,"locations":locations})

        else:
            message="No image found"
            return render(request,"search.html",{"message":message})
def copyclip(n):
    domain='https://herokupp.com'
    path=domain+n
    full_path=pyperclip.copy(path)
    return full_path
