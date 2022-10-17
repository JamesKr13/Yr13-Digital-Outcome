from calendar import FRIDAY, THURSDAY, WEDNESDAY
from lzma import FILTER_DELTA
import re
from django.db import models

# Create your models here.
from django.db import models
import PIL


class Meeting_Days(models.Model):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    periods = [("L",'Lunch'),("M",'Morning Tea')]
    Weekdays = [(MONDAY,"Monday"),(TUESDAY,'Tuesday'),(WEDNESDAY,'Wednesday'),(THURSDAY,'Thursday'),(FRIDAY,'Friday')]
    day = models.CharField(default=MONDAY,choices=Weekdays, max_length=10)
    time = models.CharField(default="2", max_length=10)
    period_name = models.CharField(default="Lunch", choices=periods,max_length=10)
    
    def weeek_period(self):
        return "%s at %s %s" % (self.day,self.period_name,self.time)
  
class Image(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')
class club(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    first_text_field = models.CharField(default="",max_length=300)
    second_text_field = models.CharField(default="",max_length=300)
    day = models.ForeignKey(Meeting_Days, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    
