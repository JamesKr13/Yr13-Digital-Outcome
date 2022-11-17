from django.shortcuts import render

# Create your views here.
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.shortcuts import redirect


def emailing(request,email,name):
    print("running code to send")
    if email and name:
        send_mail(
            'Subject here',
            'Here is the message.',
            'myclubswelly@gmail.com',
            [email],
            fail_silently=False,
        )
    redirect(request.META.HTTP_REFERER)