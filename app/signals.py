from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
@receiver(post_save, sender=Notification)
def send_notification(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        notification_obj = Notification.objects.filter(is_seen=False, owner=instance.owner).count()
        user_id = str(instance.owner.id)
        data = {
            'count':notification_obj
        }

        async_to_sync(channel_layer.group_send)(
            user_id, {
                'type':'send_notification',
                'value':json.dumps(data)
            }
        )

