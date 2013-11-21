from django.db import models

class Agent(models.Model):
    hostname = models.CharField(max_length=100)
    check_interval_ms = models.IntegerField(verbose_name='Check interval (ms)')
    last_checkin = models.DateTimeField(blank=True, null=True)
    version = models.CharField(max_length=5, blank=True, null=True)
    guid = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        verbose_name = 'Agent'
        verbose_name_plural = verbose_name + 's'
        ordering = ('hostname',)

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
    ('NOT_INSTALLED', 'Not installed'),
    ('UNKNOWN', 'Unknown'),
)
SERVICE_STATUS_DICT = dict(SERVICE_STATUS_STATES)

class WindowsService(models.Model):
    agent = models.ForeignKey('Agent', related_name='windows_services')
    service_name = models.CharField(max_length=100)
    expected_status = models.CharField(max_length=16, 
            choices=SERVICE_STATUS_STATES, default='RUNNING')

    class Meta:
        verbose_name = 'Windows Service'
        verbose_name_plural = verbose_name + 's'
        ordering = ('agent', 'service_name')

    def __unicode__(self):
        return '{self.service_name} on {self.agent}'.format(self=self)

    @property
    def latest_log_entries(self):
        return self.log.all()[:10]

    @property
    def latest_log(self):
        try:
            return self.latest_log_entries[0]
        except IndexError:
            return None

class WindowsServiceLog(models.Model):
    service = models.ForeignKey('WindowsService', related_name='log')
    timestamp = models.DateTimeField()
    expected_status = models.CharField(max_length=16)
    actual_status = models.CharField(max_length=16)
    action_taken = models.CharField(max_length=50)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Windows Service log'
        verbose_name_plural = verbose_name + 's'
        ordering = ('service', '-timestamp')

    def __unicode__(self):
        return '{service} at {timestamp}'.format(service=str(self.service), 
                timestamp=self.timestamp)

    @property
    def status_pass(self):
        return self.actual_status == self.expected_status

    @property
    def expected_status_h(self):
        return SERVICE_STATUS_DICT[self.expected_status]

    @property
    def actual_status_h(self):
        return SERVICE_STATUS_DICT[self.actual_status]
