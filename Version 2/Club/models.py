from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')
    

class Clubs(models.Model):
    club_name = models.CharField(max_length=50)
    breif = models.CharField(max_length=300)
    
class ClubImage(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    
class UserProfile(models.Model):
    club_id = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')
