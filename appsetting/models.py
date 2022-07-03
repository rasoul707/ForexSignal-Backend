from django.db import models

# Create your models here.


class AppSetting(models.Model):
    is_active_trial = models.BooleanField(
        'active trial', default=True
    )
    edit = "Edit"
