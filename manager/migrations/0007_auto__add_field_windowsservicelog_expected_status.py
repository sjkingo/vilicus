# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'WindowsServiceLog.expected_status'
        db.add_column(u'manager_windowsservicelog', 'expected_status',
                      self.gf('django.db.models.fields.CharField')(default='UNKNOWN', max_length=16),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'WindowsServiceLog.expected_status'
        db.delete_column(u'manager_windowsservicelog', 'expected_status')


    models = {
        u'manager.agent': {
            'Meta': {'ordering': "('hostname',)", 'object_name': 'Agent'},
            'check_interval_ms': ('django.db.models.fields.IntegerField', [], {}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_checkin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        u'manager.windowsservice': {
            'Meta': {'ordering': "('agent', 'service_name')", 'object_name': 'WindowsService'},
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'windows_services'", 'to': u"orm['manager.Agent']"}),
            'expected_status': ('django.db.models.fields.CharField', [], {'default': "'RUNNING'", 'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'manager.windowsservicelog': {
            'Meta': {'ordering': "('service', '-timestamp')", 'object_name': 'WindowsServiceLog'},
            'action_taken': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'actual_status': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expected_status': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'log'", 'to': u"orm['manager.WindowsService']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['manager']