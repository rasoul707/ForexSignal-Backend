from django.contrib import admin
from .models import *

# Register your models here.


class LicenseAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_private', 'unlimited', 'duration']
    fieldsets = (
        (None, {
            "fields": (
                'title', 'price', 'is_private', 'unlimited', 'duration'
            ),
        }),
    )


admin.site.register(License, LicenseAdmin)
