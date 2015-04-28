import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import WindowsServiceLog

@receiver(post_save, sender=WindowsServiceLog)
def update_last_checkin(sender, **kwargs):
    kwargs['instance'].service.agent.last_checkin = datetime.datetime.now()
    kwargs['instance'].service.agent.save()
