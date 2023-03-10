from django.db.models.signals import post_save, post_delete
from graphene_subscriptions.signals import (
    post_save_subscription,
    post_delete_subscription,
)

from .models import Chat

post_save.connect(post_save_subscription, sender=Chat, dispatch_uid="chat_post_save")
