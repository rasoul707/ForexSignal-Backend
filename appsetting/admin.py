from django.contrib import admin
from .models import *

# Register your models here.


class AppSettingAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=...):
        return False

    list_display = ['is_active_trial', 'trial_days', 'edit']
    list_display_links = ['edit']
    list_editable = ['is_active_trial', 'trial_days']


admin.site.register(AppSetting, AppSettingAdmin)
