# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20141101_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='windowsservice',
            name='restart_if_stopped',
            field=models.BooleanField(default=False),
        ),
    ]
