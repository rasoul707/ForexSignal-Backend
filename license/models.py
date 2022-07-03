from django.db import models


# Create your models here.
class License(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    description = models.TextField()
    is_private = models.BooleanField(
        "private",
        default=False,
    )
    unlimited = models.BooleanField(
        "unlimited",
        default=False,
    )
    duration = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.title

    def int(self):
        return self.id
