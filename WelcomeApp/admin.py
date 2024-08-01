# admin.py

from django.contrib import admin
from .models import SlideImage

class SlideImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)

admin.site.register(SlideImage, SlideImageAdmin)
