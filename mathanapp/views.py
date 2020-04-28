from django.shortcuts import render
import datetime as dt
from django.http import HttpResponse, Http404
from .models import Image,Category
# from .forms import ContactForm
from django.core.mail import send_mail

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

# def contactview(request):
#     name=''
#     email=''
#     comment=''

#     form= ContactForm(request.POST or None)
#     if form.is_valid():
#         name= form.cleaned_data.get("name")
#         email= form.cleaned_data.get("email")
#         comment=form.cleaned_data.get("comment")

#         if request.user.is_authenticated():
#             subject= str(request.user) + "'s Comment"
#         else:
#             subject= "A Visitor's Comment"


#         comment= name + " with the email, " + email + ", sent the following message:\n\n" + comment;
#         send_mail(subject, comment, 'klaryc4@gmail.com', [email])


#         context= {'form': form}

#         return render(request, 'contact/contact.html', context)

#     else:
#         context= {'form': form}
#         return render(request, 'contact/contact.html', context)