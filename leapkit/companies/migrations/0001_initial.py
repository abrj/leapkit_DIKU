# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Industry'
        db.create_table(u'companies_industry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'companies', ['Industry'])

        # Adding model 'Company'
        db.create_table(u'companies_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='company_country', null=True, to=orm['geographic_info.Country'])),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='company_region', null=True, to=orm['geographic_info.Region'])),
            ('zip_code', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='company_zipcode', null=True, to=orm['geographic_info.ZipCode'])),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='company_city', null=True, to=orm['geographic_info.City'])),
            ('street', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='company_street', null=True, to=orm['geographic_info.Street'])),
            ('company_size', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('year_founded', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('industry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['companies.Industry'])),
            ('about', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('overview', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('mission', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('projects_available', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('projects_latest_buying_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('projects_former_buying_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'companies', ['Company'])

        # Adding model 'CompanyProject'
        db.create_table(u'companies_companyproject', (
            (u'project_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['projects.Project'], unique=True, primary_key=True)),
            ('project_owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['companies.Company'])),
            ('payment', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('web_page', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('involvement', self.gf('django.db.models.fields.IntegerField')()),
            ('nda_required', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
        ))
        db.send_create_signal(u'companies', ['CompanyProject'])

        # Adding model 'ProjectPackages'
        db.create_table(u'companies_projectpackages', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('buying_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('payed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'companies', ['ProjectPackages'])


    def backwards(self, orm):
        # Deleting model 'Industry'
        db.delete_table(u'companies_industry')

        # Deleting model 'Company'
        db.delete_table(u'companies_company')

        # Deleting model 'CompanyProject'
        db.delete_table(u'companies_companyproject')

        # Deleting model 'ProjectPackages'
        db.delete_table(u'companies_projectpackages')


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
            'city': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'company_city'", 'null': 'True', 'to': u"orm['geographic_info.City']"}),
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
            'street': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'company_street'", 'null': 'True', 'to': u"orm['geographic_info.Street']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'year_founded': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'company_zipcode'", 'null': 'True', 'to': u"orm['geographic_info.ZipCode']"})
        },
        u'companies.companyproject': {
            'Meta': {'ordering': "['created', 'start_date', 'title']", 'object_name': 'CompanyProject', '_ormbases': [u'projects.Project']},
            'involvement': ('django.db.models.fields.IntegerField', [], {}),
            'nda_required': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'payment': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'project_owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['companies.Company']"}),
            u'project_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['projects.Project']", 'unique': 'True', 'primary_key': 'True'}),
            'web_page': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'companies.industry': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Industry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'companies.projectpackages': {
            'Meta': {'object_name': 'ProjectPackages'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'buying_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payed': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'geographic_info.city': {
            'Meta': {'ordering': "('region', 'name')", 'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographic_info.Region']"})
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
        u'geographic_info.street': {
            'Meta': {'ordering': "('city', 'name')", 'object_name': 'Street'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographic_info.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        },
        u'geographic_info.zipcode': {
            'Meta': {'ordering': "('zip_code',)", 'object_name': 'ZipCode'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographic_info.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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

    complete_apps = ['companies']