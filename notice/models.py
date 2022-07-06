from django.db import models

# Create your models here.


class Broker(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    logo = models.ForeignKey(
        "upload.Image", on_delete=models.SET_NULL, blank=False, null=False,
    )

    def __str__(self):
        return self.name


class SignalAlert(models.Model):
    broker = models.ForeignKey(
        Broker, on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)

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
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
