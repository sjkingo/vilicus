# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=100)),
                ('check_interval_ms', models.IntegerField(verbose_name=b'Check interval (ms)')),
                ('last_checkin', models.DateTimeField(null=True, blank=True)),
                ('version', models.CharField(max_length=5, null=True, blank=True)),
                ('guid', models.CharField(max_length=40, null=True, blank=True)),
            ],
            options={
                'ordering': ('hostname',),
                'verbose_name': 'Agent',
                'verbose_name_plural': 'Agents',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PerformanceLogEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField()),
                ('cpu_usage', models.IntegerField()),
                ('agent', models.ForeignKey(related_name='perflogs', to='manager.Agent')),
            ],
            options={
                'ordering': ('agent', '-timestamp'),
                'verbose_name': 'Performance log entry',
                'verbose_name_plural': 'Performance log entries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WindowsService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('service_name', models.CharField(max_length=100)),
                ('expected_status', models.CharField(default=b'RUNNING', max_length=16, choices=[(b'START_PENDING', b'Start pending'), (b'RUNNING', b'Running'), (b'STOP_PENDING', b'Stop pending'), (b'STOPPED', b'Stopped'), (b'PAUSE_PENDING', b'Pause pending'), (b'PAUSED', b'Paused'), (b'CONTINUE_PENDING', b'Continue pending'), (b'NOT_INSTALLED', b'Not installed'), (b'UNKNOWN', b'Unknown')])),
                ('hidden', models.BooleanField()),
                ('agent', models.ForeignKey(related_name='windows_services', to='manager.Agent')),
            ],
            options={
                'ordering': ('agent', 'description', 'service_name'),
                'verbose_name': 'Windows Service',
                'verbose_name_plural': 'Windows Services',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WindowsServiceLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField()),
                ('expected_status', models.CharField(max_length=16)),
                ('actual_status', models.CharField(max_length=16)),
                ('action_taken', models.CharField(max_length=50)),
                ('comments', models.TextField(null=True, blank=True)),
                ('service', models.ForeignKey(related_name='log', to='manager.WindowsService')),
            ],
            options={
                'ordering': ('service', '-timestamp'),
                'verbose_name': 'Windows Service log',
                'verbose_name_plural': 'Windows Service logs',
            },
            bases=(models.Model,),
        ),
    ]
