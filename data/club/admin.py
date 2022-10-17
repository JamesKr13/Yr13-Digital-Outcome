from django.contrib import admin

# Register your models here.

from .models import club
from .models import Image

class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo"]

admin.site.register(Image, imageAdmin)
admin.site.register(club)