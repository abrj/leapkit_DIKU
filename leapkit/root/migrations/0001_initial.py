# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'root_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('answer', self.gf('django.db.models.fields.TextField')()),
            ('subject', self.gf('django.db.models.fields.CharField')(default='S', max_length=1)),
        ))
        db.send_create_signal(u'root', ['Question'])

        # Adding model 'UserQuery'
        db.create_table(u'root_userquery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('has_been_answered', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('answer', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'root', ['UserQuery'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'root_question')

        # Deleting model 'UserQuery'
        db.delete_table(u'root_userquery')


    models = {
        u'root.question': {
            'Meta': {'ordering': "['subject', 'question']", 'object_name': 'Question'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'subject': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'})
        },
        u'root.userquery': {
            'Meta': {'ordering': "['created']", 'object_name': 'UserQuery'},
            'answer': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'has_been_answered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['root']