# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'projects_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('contact_person', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('contact_phone', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('project_length', self.gf('django.db.models.fields.FloatField')()),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('students_needed', self.gf('django.db.models.fields.IntegerField')()),
            ('full_description', self.gf('django.db.models.fields.TextField')()),
            ('short_description', self.gf('django.db.models.fields.TextField')(max_length=250)),
            ('project_document', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('views', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('project_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('education_requirements', self.gf('django.db.models.fields.CharField')(default='ALL', max_length=3)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'projects', ['Project'])

        # Adding M2M table for field country_requirements on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_country_requirements')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('country', models.ForeignKey(orm[u'geographic_info.country'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'country_id'])

        # Adding M2M table for field region_requirements on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_region_requirements')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('region', models.ForeignKey(orm[u'geographic_info.region'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'region_id'])

        # Adding M2M table for field course_requirements on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_course_requirements')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('course', models.ForeignKey(orm[u'institutions.course'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'course_id'])

        # Adding M2M table for field university_requirements on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_university_requirements')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('institution', models.ForeignKey(orm[u'institutions.institution'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'institution_id'])

        # Adding M2M table for field related_lines_of_study on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_related_lines_of_study')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('fieldofstudy', models.ForeignKey(orm[u'institutions.fieldofstudy'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'fieldofstudy_id'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'projects_project')

        # Removing M2M table for field country_requirements on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_country_requirements'))

        # Removing M2M table for field region_requirements on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_region_requirements'))

        # Removing M2M table for field course_requirements on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_course_requirements'))

        # Removing M2M table for field university_requirements on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_university_requirements'))

        # Removing M2M table for field related_lines_of_study on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_related_lines_of_study'))


    models = {
        u'geographic_info.country': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Country'},
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        },
        u'geographic_info.region': {
            'Meta': {'ordering': "('country', 'name')", 'object_name': 'Region'},
            'area_code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographic_info.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        },
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
        },
        u'projects.project': {
            'Meta': {'ordering': "['created', 'start_date', 'title']", 'object_name': 'Project'},
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'country_requirements': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['geographic_info.Country']", 'null': 'True', 'blank': 'True'}),
            'course_requirements': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['institutions.Course']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'education_requirements': ('django.db.models.fields.CharField', [], {'default': "'ALL'", 'max_length': '3'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'full_description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'project_document': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'project_length': ('django.db.models.fields.FloatField', [], {}),
            'project_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'region_requirements': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['geographic_info.Region']", 'null': 'True', 'blank': 'True'}),
            'related_lines_of_study': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Related Lines of Study'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['institutions.FieldOfStudy']"}),
            'short_description': ('django.db.models.fields.TextField', [], {'max_length': '250'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'students_needed': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'university_requirements': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['institutions.Institution']", 'null': 'True', 'blank': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        }
    }

    complete_apps = ['projects']