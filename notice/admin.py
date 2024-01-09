from django.contrib import admin
from .models import *
# Register your models here.


class SignalAlertAdmin(admin.ModelAdmin):

    list_display = ['title', 'broker', 'percent', 'winrate', 'is_active', 'detail', 'description']
    list_editable = ['percent', 'winrate', 'is_active', 'detail']

admin.site.register(Broker)
admin.site.register(SignalAlert, SignalAlertAdmin)
