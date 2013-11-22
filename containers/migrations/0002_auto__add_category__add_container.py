# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('containers_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Category_name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('containers', ['Category'])

        # Adding model 'Container'
        db.create_table('containers_container', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('serial_Number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('container_Status', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_Inspection_Date', self.gf('django.db.models.fields.DateField')()),
            ('next_Inspection_Date', self.gf('django.db.models.fields.DateField')()),
            ('date_Rented', self.gf('django.db.models.fields.DateField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['containers.Category'])),
        ))
        db.send_create_signal('containers', ['Container'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('containers_category')

        # Deleting model 'Container'
        db.delete_table('containers_container')


    models = {
        'containers.category': {
            'Category_name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {})
        },
        'containers.container': {
            'Meta': {'object_name': 'Container'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['containers.Category']"}),
            'container_Status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date_Rented': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_Inspection_Date': ('django.db.models.fields.DateField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'next_Inspection_Date': ('django.db.models.fields.DateField', [], {}),
            'serial_Number': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['containers']