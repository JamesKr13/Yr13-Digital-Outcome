from django.shortcuts import render
import random
from django.core import serializers
# Create your views here.
from django.shortcuts import render
from .models import Image,Clubs,ClubImage
from json import dumps

# Create your views here.
def index(request):
    data = Image.objects.all()
    context = {
        'data' : data
    }
    return render(request,"display.html", )

def GetRandomClub(request):
    clubs = Clubs.objects.all()
    random_clubs = list(set([random.randint(0,clubs.count()),
                    random.randint(0,clubs.count()).
                    random.randint(0,clubs.count()),
                    random.randint(0,clubs.count()),
                    random.randint(0,clubs.count())]))
    response_clubs = [dumps(clubs[pk]) for pk in random_clubs]
    dataJSON = {}
    for tb_json_index in range(0,response_clubs.len()):
        dataJSON["data"+str(tb_json_index)] = response_clubs[tb_json_index]
    dataJSON["test"] = clubs[0]
    return render(request,'spa/index.html',{"test":dumps(clubs[0].get().breif)})
    
    
    

# def post_clubs(request):
#     if request.is_ajax() and request.method == "POST":
#         club = Clubs(request.POST)
        