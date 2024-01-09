from django.contrib import admin
from .models import *
from django_object_actions import DjangoObjectActions, action

# Register your models here.


class SignalAlertAdmin(DjangoObjectActions, admin.ModelAdmin):

    list_display = ['title', 'description', 'broker', 'percent', 'winrate', 'is_active', 'detail']
    list_editable = ['percent', 'winrate', 'is_active', 'detail']

    @action(label="Delete All History")
    def delete_history(modeladmin, request, queryset):
        queryset.update(is_active=False)
    changelist_actions = ('delete_history', )



admin.site.register(Broker)
admin.site.register(SignalAlert, SignalAlertAdmin)
