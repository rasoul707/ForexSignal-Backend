from django.db import models

# Create your models here.


class AppSetting(models.Model):
    is_active_trial = models.BooleanField(
        'active trial', default=True
    )
    trial_license = models.ForeignKey(
        "license.License", on_delete=models.SET_NULL, default=1, null=True
    )
    pay_description = models.TextField(default="توضیحات پرداخت")
    terms = models.TextField(default="قوانین")
    percent = models.DecimalField(max_digits=6, decimal_places=1, default=2.5, blank=False, null=False)
    winrate = models.DecimalField(max_digits=6, decimal_places=1, default=80, blank=False, null=False)
    edit = "Edit"
