# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PushoverUserTokens',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('token', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Pushover user token',
                'verbose_name_plural': 'Pushover user tokens',
            },
            bases=(models.Model,),
        ),
    ]
