from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class LoginForm(AuthenticationForm):
    """user login form"""
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'pss',
                'placeholder': 'Password',
            }))
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'my-class',
                'placeholder': 'UserName',
            }))