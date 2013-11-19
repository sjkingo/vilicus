from django.db import models

class Agent(models.Model):
    hostname = models.CharField(max_length=100)
    last_checkin = models.DateTimeField(blank=True, null=True)
