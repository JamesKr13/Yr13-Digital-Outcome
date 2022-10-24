from django.shortcuts import render
import random
from django.core import serializers
# Create your views here.
from django.shortcuts import render
from .models import Image,Clubs,ClubImage
from json import dumps

# Create your views here.
from django.views.generic import TemplateView
from django.template.response   import TemplateResponse
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Clubs,ClubImage
from django import template

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
    all_data = Clubs.objects.order_by('?')[:9]
    data = all_data[0:6]
    c_data = all_data[6:9]
    image = []
    for club in data:
        try:
            image.append(ClubImage.objects.filter(club=club)[0])
        except IndexError:
            image.append("")
    c_images = []     
    for club in c_data:
        try:
            c_images.append(ClubImage.objects.filter(club=club)[0])
        except IndexError:
            c_images.append("")
    return render(request,'spa/index.html',{"clubs": data,"images": image,"c_clubs": c_data,"c_images":c_images})
       
        

    # def post_clubs(request):
    #     if request.is_ajax() and request.method == "POST":
    #         club = Clubs(request.POST)
