from django.db.models.signals import post_save
from django.dispatch import receiver

from manager.models import WindowsServiceLog
from .send import *

class LastStatusDummy(object):
    actual_status = '(None)'

@receiver(post_save, sender=WindowsServiceLog)
def log_post_save(sender, **kwargs):
    inst = kwargs['instance']
    if inst.service.changed_since_last:
        status_now = inst.service.latest_log_entries[0]
        try:
            last_status = inst.service.latest_log_entries[1]
        except IndexError:
            last_status = LastStatusDummy()

        title = '{name} is now {now}'.format(name=inst.service, now=status_now.actual_status)
        msg = 'The service {name} running on {agent} has just changed status from {last} -> {now} at {dt}'.format(
                name=inst.service, agent=inst.service.agent.hostname, 
                last=last_status.actual_status, now=status_now.actual_status,
                dt=status_now.timestamp)

        send_push_notification(title, msg, priority=PRIORITY['HIGH'])
