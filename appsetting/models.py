from django.db import models

# Create your models here.


class AppSetting(models.Model):
    is_active_trial = models.BooleanField(
        'active trial', default=True
    )
    trial_days = models.IntegerField(
        'trial days', blank=False, null=False, default=1
    )
    edit = "Edit"
