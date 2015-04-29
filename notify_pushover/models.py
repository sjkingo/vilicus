from django.db import models

class PushoverUserTokens(models.Model):
    email = models.EmailField(max_length=254)
    token = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    class Meta:
        app_label = 'notify_pushover'
        verbose_name = 'Pushover user token'
        verbose_name_plural = verbose_name + 's'

    def __unicode__(self):
        return self.email + ': ' + self.token

