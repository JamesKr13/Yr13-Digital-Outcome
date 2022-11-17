from django.shortcuts import render

# from django.conf import settings
# from django.core.mail import BadHeaderError, send_mail
# from django.http import HttpResponse, HttpResponseRedirect
# # Create your views here.
# def send_email(name, email):
#     subject = "Request to join you're club"
#     message =  name+" has shown interest in joining your club"
#     from_email = email
#     if subject and message and from_email:
#         try:
#             send_mail(subject, message, from_email, ['myclubswelly@gmail.com'])
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return HttpResponseRedirect('/contact/thanks/')
#     else:
#         # In reality we'd use a form class
#         # to get proper validation errors.
#         return HttpResponse('Make sure all fields are entered and valid.')
    