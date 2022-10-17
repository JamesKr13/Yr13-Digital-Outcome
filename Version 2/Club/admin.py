

# Register your models here.
from django.contrib import admin
from .models import Clubs, Image,ClubImage

class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo"]

admin.site.register(Image, imageAdmin)
admin.site.register(ClubImage)
admin.site.register(Clubs)
