from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class ClubForm(AuthenticationForm):
    """user login form"""
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'CustomUser',
                'placeholder': 'Password',
            }))
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'CustomUser',
                'placeholder': 'UserName',
            }))