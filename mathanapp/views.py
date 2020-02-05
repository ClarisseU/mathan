from django.shortcuts import render
import datetime as dt
from django.http import HttpResponse, Http404
from .models import Image,Category

# Create your views here.
def welcome(request):
    images = Image.objects.all()
    
    return render(request, 'index.html',{'image':images})

def image(request,id):
    try:
        images= Image.objects.get(id = id)
    except DoesNotExist:
        raise Http404()
    return render(request,'all-photos/image.html',{'image':images}) 

def all_images(request):
    images = Image.objects.all()
    return render(request, 'all_images.html',{'images':images})

def category(request, category):
    image = Image.filter_by_category(category)
    category = Category.objects.all()
    return render(request,'all-photos/category.html',{'category':category, 'image':image})