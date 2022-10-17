from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class UserAccessView(TemplateView):
    template_name = "user-access/login.html"