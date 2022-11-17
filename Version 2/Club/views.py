from django.shortcuts import render
import random
from django.core import serializers
# Create your views here.
from django.shortcuts import render
from .models import Image,Clubs,ClubImage
from json import dumps
from django.template.defaultfilters import stringfilter
# Create your views here.
from django.views.generic import TemplateView
from django.template.response   import TemplateResponse
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Clubs,ClubImage
from django import template
from .forms import ClubForm
from accounts.models import CustomUser
from django.contrib.auth.models import User
from accounts.models import CustomUser
from myapp.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
register = template.Library()


def load_clubs(request, name):
    club = Clubs.objects.filter(club_name=name)[0]
    images = ClubImage.objects.filter(club=club)
    context = {
            'Name' : club.club_name,
            'breif' : club.breif,
            'Images':  images
        }
    return render(request,"Club/generic_club_page.html", context)
class ClubView(TemplateView):
    template_name = "Club/generic_club_page.html"
    
    
    def index(request):
        data = Image.objects.all()
        context = {
            'data' : data
        }
        return render(request,"display.html", )
    def show(request):
        # Get query_name from request
        query = Clubs.objects.all()
        c = {
            'data' : query
        }
        t = loader.get_template('myapp/index.html')
        return HttpResponse(t.render(c, request))

def get_random_club(request):
    all_data = Clubs.objects.order_by('?')[:10]
    data = all_data[0:6]
    c_data = all_data[6:10]
    image = []
    for club in data:
        try:
            image.append(ClubImage.objects.filter(club=club)[0])
        except IndexError:
            image.append("")
    c_images = []     
    car_img_clubs = []
    for club in c_data:
        try:
            c_images.append(ClubImage.objects.filter(club=club)[0])
            
            
        except IndexError:
            c_images.append("")
    return render(request,'spa/index.html',{"clubs": data,"images": image,"c_clubs": c_data,"c_images":c_images})
       
        
def intrest(request):
    sub = forms.Interest()
    if request.method == 'POST':
        sub = forms.Interest(request.POST)
        subject = 'Someone shown interest in your club'
        message = 'You ha'
        recepient = str(sub['Email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form':sub})
    # def post_clubs(request):
    #     if request.is_ajax() and request.method == "POST":
    #         club = Clubs(request.POST)

# register.filter("search",search)
def searching(request,string):
    clubs = Clubs.objects.all()
    c_data = {}
    i_data = []
    for club in clubs:
        if string.lower() in club.club_name.lower():
            i_data.append(club)
    return render(request,'spa/index.html',{"clubs": i_data})


def club_form(request):
    form = ClubForm(request.POST, request.FILES)
    if form.is_valid():
        saved=form.save()
        img_obj = saved[1]
        return render(request, "CreateAClub.html", {'form': form, 'img_obj': img_obj})
    else:
        form = ClubForm()
    return render(request, 'CreateAClub.html', {'form': form})



# def delete(request, user):
#     club = CustomUser.objects.filter()