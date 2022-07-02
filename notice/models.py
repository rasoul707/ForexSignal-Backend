from django.db import models
from realtime.consumers import SignalsAlertWS

# Create your models here.


class Broker(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    logo = models.ForeignKey(
        "upload.Image", on_delete=models.SET_NULL, blank=True, null=True,
    )

    def __str__(self):
        return self.name


class SignalAlert(models.Model):
    broker = models.ForeignKey(
        Broker, on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    users_received = models.ManyToManyField(
        "authentication.Account", blank=True,
    )
    is_active = models.BooleanField('active', default=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(
        "upload.Image", on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        ordering = ['-id']

    def save(self, *args, **kwargs):
        print('yyyyy')
        SignalsAlertWS.send(SignalsAlertWS)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
