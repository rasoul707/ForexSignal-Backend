from django.db import models

# Create your models here.


class Broker(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    logo = models.ForeignKey(
        "upload.Image", on_delete=models.CASCADE, blank=False, null=False,
    )

    def __str__(self):
        return self.name


class SignalAlert(models.Model):
    broker = models.ForeignKey(
        Broker, on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    percent = models.DecimalField(max_digits=6, decimal_places=1, default=2.5, blank=False, null=False)
    winrate = models.DecimalField(max_digits=6, decimal_places=1, default=80, blank=False, null=False)
    detail = models.TextField(blank=True, null=True)

    success = models.BooleanField('success', null=True)

    is_active = models.BooleanField('active', default=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_datetime']

    def save(self, *args, **kwargs):
        from asgiref.sync import async_to_sync
        from .serializers import SignalAlertSerializer
        from channels.layers import get_channel_layer
        serializer = SignalAlertSerializer(self)
        room_name = 'signal' + str(serializer.data['broker_id'])
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(room_name, {
            'type': 'send_alert',
            'data': serializer.data,
        })
        super().save(*args, **kwargs)
        return self

    def __str__(self):
        return self.title

    def int(self):
        return self.id
