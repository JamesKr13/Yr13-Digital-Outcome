from django import template
from django.template.defaultfilters import stringfilter
from Club.models import Clubs, ClubImage
import json
from django.forms.models import model_to_dict
import os
from django.utils.safestring import SafeString
from django.utils.safestring import mark_safe
register = template.Library()


from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
# @register.simple_tag
# def user():
#     if user


@register.simple_tag
def send_email(name, email):
    pass
    # subject = "Request to join you're club"
    # message =  name+" has shown interest in joining your club"
    # from_email = email
    # if subject and message and from_email:
    #     try:
    #         send_mail(subject, message, from_email, ['myclubswelly@gmail.com'])
    #     except BadHeaderError:
    #         return HttpResponse('Invalid header found.')
    #     return HttpResponseRedirect('/contact/thanks/')
    # else:
    #     # In reality we'd use a form class
    #     # to get proper validation errors.
    #     return HttpResponse('Make sure all fields are entered and valid.')
@register.filter(is_safe=True)
@register.simple_tag
@register.filter(name='Search', is_safe=True)
def search(value):
    clubs = Clubs.objects.all()
    c_data = []
    i_data = []
    for club in clubs:
        if value.lower() in club.club_name.lower():
             c_data.append([club.club_name,club.breif,ClubImage.objects.filter(club=club)[0].photo.name])
            # i_data.append(ClubImage.objects.filter(club=club)[0].photo.name)
    return mark_safe(c_data)
 
@register.filter(name='get_color')
def color(value):
    if value:
        return "#FF0000" 

# def search(search_str):
#     clubs = Clubs.objects.all()
#     output = []

#     for club in clubs:
#         if search_str in club.club_name:
#             output.append([json.dumps(model_to_dict(club)),json.dumps(model_to_dict(ClubImage.objects.filter(club=club)[0].photo))])
#     return output
