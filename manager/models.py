from django.db import models

class Agent(models.Model):
    hostname = models.CharField(max_length=100)
    check_interval_ms = models.IntegerField(verbose_name='Check interval (ms)')
    last_checkin = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Agent'
        verbose_name_plural = verbose_name + 's'

    def __unicode__(self):
        return self.hostname
