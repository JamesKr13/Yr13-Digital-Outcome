from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.
def logout_user(request):
    auth.logout(request)
    return redirect('/home')