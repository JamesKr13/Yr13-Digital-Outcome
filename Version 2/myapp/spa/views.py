from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class SpaView(TemplateView):
    template_name = "spa/index.html"