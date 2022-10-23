from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
import random
from Club.views import get_random_club

def SpaView(request):
    # template_name = "spa/app.html"
    return get_random_club(request)

 
        