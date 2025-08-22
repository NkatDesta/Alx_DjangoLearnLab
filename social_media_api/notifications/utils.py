from .models import Notification

def create_notification(actor, recipient, verb, target):
    if actor != recipient:  # Avoid notifying oneself
        Notification.objects.create(
            actor=actor,
            recipient=recipient,
            verb=verb,
            target=target
        )
