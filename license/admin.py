from django.contrib import admin
from .models import *

# Register your models here.


class LicenseAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'description', 'is_active', 'unlimited']


admin.site.register(License, LicenseAdmin)
