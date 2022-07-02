
from pydoc import describe
from django.db import models
import datetime


# Create your models here.
class License(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    description = models.TextField()
    is_active = models.BooleanField(
        "active",
        default=True,
    )
    unlimited = models.BooleanField(
        "unlimited",
        default=False,
    )
    duration = models.DurationField()

    def __str__(self):
        return self.title
