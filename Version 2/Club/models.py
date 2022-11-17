from django.db import models
from django.conf import settings
from django.core import serializers# Create your models here.
import re

class Image(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')
    

class Clubs(models.Model):
    # owner = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    # )
    club_name = models.CharField(max_length=50)
    breif = models.CharField(max_length=300)
    
    def __str__(self):
        return self.club_name

class ClubImage(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')
    
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    
class UserProfile(models.Model):
    club_id = models.CharField(max_length=20)
    photo = models.ImageField(null=True, blank=True,upload_to='pics')
    
    def __str__(self):
        return self.photo.url
