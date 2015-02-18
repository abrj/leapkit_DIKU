# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FAQuestion'
        db.create_table(u'queries_faquestion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('answer', self.gf('django.db.models.fields.TextField')()),
            ('subject', self.gf('django.db.models.fields.CharField')(default='S', max_length=1)),
        ))
        db.send_create_signal(u'queries', ['FAQuestion'])

        # Adding model 'UserQuestion'
        db.create_table(u'queries_userquestion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('has_been_answered', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('answer', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'queries', ['UserQuestion'])


    def backwards(self, orm):
        # Deleting model 'FAQuestion'
        db.delete_table(u'queries_faquestion')

        # Deleting model 'UserQuestion'
        db.delete_table(u'queries_userquestion')


    models = {
        u'queries.faquestion': {
            'Meta': {'ordering': "['subject', 'question']", 'object_name': 'FAQuestion'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'subject': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'})
        },
        u'queries.userquestion': {
            'Meta': {'ordering': "['created']", 'object_name': 'UserQuestion'},
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

    complete_apps = ['queries']