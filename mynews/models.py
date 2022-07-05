from django.db import models

# Create your models here.

NewsStatusTypes = (
    ('draft', 'Draft'),
    ('publish', 'Publish'),
)


class MyNews(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    excerpt = models.TextField(blank=False, null=False, verbose_name="خلاصه")
    content = models.TextField(blank=False, null=False)
    image = models.ForeignKey(
        "upload.Image", on_delete=models.SET_NULL, blank=True, null=True,
    )
    created_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100, choices=NewsStatusTypes, default='publish'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_datetime']

    def save(self, *args, **kwargs):
        from asgiref.sync import async_to_sync
        from .serializers import MyNewsSerializer
        from channels.layers import get_channel_layer
        serializer = MyNewsSerializer(self)
        room_name = 'news'
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(room_name, {
            'type': 'send_news',
            'data': serializer.data,
        })
        return super().save(*args, **kwargs)
