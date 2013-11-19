from django.db import models

class Agent(models.Model):
    hostname = models.CharField(max_length=100)
    last_checkin = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Agent'
        verbose_name_plural = verbose_name + 's'

    def __unicode__(self):
        return self.hostname
