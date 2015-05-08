# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ProjectPackage.note'
        db.add_column(u'companies_projectpackage', 'note',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ProjectPackage.note'
        db.delete_column(u'companies_projectpackage', 'note')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'companies.company': {
            'Meta': {'object_name': 'Company'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '254', 'blank': 'True'}),
            'company_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'company_country'", 'null': 'True', 'to': u"orm['geographic_info.Country']"}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['companies.Industry']"}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'mission': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'overview': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'projects_available': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'projects_former_buying_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'projects_latest_buying_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'company_region'", 'null': 'True', 'to': u"orm['geographic_info.Region']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'year_founded': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'companies.companyproject': {
            'Meta': {'ordering': "['created', 'start_date', 'title']", 'object_name': 'CompanyProject', '_ormbases': [u'projects.Project']},
            'involvement': ('django.db.models.fields.IntegerField', [], {}),
            'nda_required': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'payment': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'project_owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['companies.Company']"}),
            u'project_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['projects.Project']", 'unique': 'True', 'primary_key': 'True'}),
            'resume_required': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'thesis_or_internship_required': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '2', 'blank': 'True'}),
            'web_page': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'companies.industry': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Industry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'companies.projectpackage': {
            'Meta': {'object_name': 'ProjectPackage'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '254', 'blank': 'True'}),
            'buying_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'payment_received': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'Meta': {'ordering': "('number_of_students', 'name')", 'object_name': 'Institution'},
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
        u'projects.jobfunction': {
            'Meta': {'object_name': 'JobFunction'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'})
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
            'job_functions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Related job functions'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['projects.JobFunction']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'open_for_applications': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'project_document': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'project_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'region_requirements': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['geographic_info.Region']", 'null': 'True', 'blank': 'True'}),
            'related_lines_of_study': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Related Lines of Study'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['institutions.FieldOfStudy']"}),
            'short_description': ('django.db.models.fields.TextField', [], {'max_length': '250'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'students_needed': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'university_requirements': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['institutions.Institution']", 'null': 'True', 'blank': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        }
    }

    complete_apps = ['companies']