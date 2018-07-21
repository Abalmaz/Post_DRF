from posts.models import Post
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
import channels.layers
from asgiref.sync import async_to_sync
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=Post)
def send_post(sender, instance=None, created=False, **kwargs):
    if created:
        channel_layer = channels.layers.get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'current_user', {
                'type': 'new_post',
                'message': instance.pk,
            }
        )

