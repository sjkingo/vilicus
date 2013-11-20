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

# From http://msdn.microsoft.com/en-us/library/windows/desktop/ee126211(v=vs.85).aspx
SERVICE_STATUS_STATES = (
    ('START_PENDING', 'Start pending'),
    ('RUNNING', 'Running'),
    ('STOP_PENDING', 'Stop pending'),
    ('STOPPED', 'Stopped'),
    ('PAUSE_PENDING', 'Pause pending'),
    ('PAUSED', 'Paused'),
    ('CONTINUE_PENDING', 'Continue pending'),
)

class Service(models.Model):
    agent = models.ForeignKey('Agent', related_name='services')
    service_name = models.CharField(max_length=100)
    expected_status = models.CharField(max_length=16, 
            choices=SERVICE_STATUS_STATES, default='RUNNING')

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = verbose_name + 's'

    def __unicode__(self):
        return '{self.service_name} on {self.agent}'.format(self=self)
