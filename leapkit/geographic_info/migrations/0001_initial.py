# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'geographic_info_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('country_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'geographic_info', ['Country'])

        # Adding model 'Region'
        db.create_table(u'geographic_info_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geographic_info.Country'])),
            ('area_code', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'geographic_info', ['Region'])

        # Adding model 'City'
        db.create_table(u'geographic_info_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geographic_info.Region'])),
        ))
        db.send_create_signal(u'geographic_info', ['City'])

        # Adding model 'ZipCode'
        db.create_table(u'geographic_info_zipcode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geographic_info.City'])),
        ))
        db.send_create_signal(u'geographic_info', ['ZipCode'])

        # Adding model 'Street'
        db.create_table(u'geographic_info_street', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geographic_info.City'])),
        ))
        db.send_create_signal(u'geographic_info', ['Street'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table(u'geographic_info_country')

        # Deleting model 'Region'
        db.delete_table(u'geographic_info_region')

        # Deleting model 'City'
        db.delete_table(u'geographic_info_city')

        # Deleting model 'ZipCode'
        db.delete_table(u'geographic_info_zipcode')

        # Deleting model 'Street'
        db.delete_table(u'geographic_info_street')


    models = {
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
        }
    }

    complete_apps = ['geographic_info']