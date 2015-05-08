# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'root_question')

        # Deleting model 'UserQuery'
        db.delete_table(u'root_userquery')


    def backwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'root_question', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('answer', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(default='S', max_length=1)),
        ))
        db.send_create_signal(u'root', ['Question'])

        # Adding model 'UserQuery'
        db.create_table(u'root_userquery', (
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('answer', self.gf('django.db.models.fields.TextField')(default='')),
            ('has_been_answered', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'root', ['UserQuery'])


    models = {
        
    }

    complete_apps = ['root']