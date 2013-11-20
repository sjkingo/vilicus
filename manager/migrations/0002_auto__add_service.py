# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Service'
        db.create_table(u'manager_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('agent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='services', to=orm['manager.Agent'])),
            ('service_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('expected_status', self.gf('django.db.models.fields.CharField')(default='RUNNING', max_length=16)),
        ))
        db.send_create_signal(u'manager', ['Service'])


    def backwards(self, orm):
        # Deleting model 'Service'
        db.delete_table(u'manager_service')


    models = {
        u'manager.agent': {
            'Meta': {'object_name': 'Agent'},
            'check_interval_ms': ('django.db.models.fields.IntegerField', [], {}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_checkin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'manager.service': {
            'Meta': {'object_name': 'Service'},
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'services'", 'to': u"orm['manager.Agent']"}),
            'expected_status': ('django.db.models.fields.CharField', [], {'default': "'RUNNING'", 'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['manager']