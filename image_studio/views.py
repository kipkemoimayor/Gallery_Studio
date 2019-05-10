from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    message='Be  am beated'
    return render(request,"index.html",{'message':message})
