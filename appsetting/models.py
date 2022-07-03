from django.db import models

# Create your models here.


class AppSetting(models.Model):
    is_active_trial = models.BooleanField(
        'active trial', default=True
    )
    trial_license = models.ForeignKey(
        "license.License", on_delete=models.SET_NULL, default=1, null=True
    )
    edit = "Edit"
