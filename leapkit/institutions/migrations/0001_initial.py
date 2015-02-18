# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Institution'
        db.create_table(u'institutions_institution', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('number_of_students', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'institutions', ['Institution'])

        # Adding model 'Department'
        db.create_table(u'institutions_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('university', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['institutions.Institution'])),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
        ))
        db.send_create_signal(u'institutions', ['Department'])

        # Adding model 'Professor'
        db.create_table(u'institutions_professor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'institutions', ['Professor'])

        # Adding model 'Course'
        db.create_table(u'institutions_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['institutions.Department'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('ects_points', self.gf('django.db.models.fields.FloatField')()),
            ('professor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['institutions.Professor'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('learning_goals', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('learning_activities', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('obligatory_activities', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('evaluation_form', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'institutions', ['Course'])

        # Adding model 'FieldOfStudy'
        db.create_table(u'institutions_fieldofstudy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'institutions', ['FieldOfStudy'])


    def backwards(self, orm):
        # Deleting model 'Institution'
        db.delete_table(u'institutions_institution')

        # Deleting model 'Department'
        db.delete_table(u'institutions_department')

        # Deleting model 'Professor'
        db.delete_table(u'institutions_professor')

        # Deleting model 'Course'
        db.delete_table(u'institutions_course')

        # Deleting model 'FieldOfStudy'
        db.delete_table(u'institutions_fieldofstudy')


    models = {
        u'institutions.course': {
            'Meta': {'ordering': "('department', 'name')", 'object_name': 'Course'},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['institutions.Department']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ects_points': ('django.db.models.fields.FloatField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'evaluation_form': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'learning_activities': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'learning_goals': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'obligatory_activities': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'professor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['institutions.Professor']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'institutions.department': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Department'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'university': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['institutions.Institution']"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'institutions.fieldofstudy': {
            'Meta': {'object_name': 'FieldOfStudy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'institutions.institution': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Institution'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number_of_students': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'institutions.professor': {
            'Meta': {'object_name': 'Professor'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['institutions']