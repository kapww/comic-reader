# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comic'
        db.create_table(u'comics_comic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('web_url', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'comics', ['Comic'])

        # Adding model 'ComicInstance'
        db.create_table(u'comics_comicinstance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['comics.Comic'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('number', self.gf('django.db.models.fields.IntegerField')(default=-1)),
        ))
        db.send_create_signal(u'comics', ['ComicInstance'])


    def backwards(self, orm):
        # Deleting model 'Comic'
        db.delete_table(u'comics_comic')

        # Deleting model 'ComicInstance'
        db.delete_table(u'comics_comicinstance')


    models = {
        u'comics.comic': {
            'Meta': {'object_name': 'Comic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'web_url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'comics.comicinstance': {
            'Meta': {'object_name': 'ComicInstance'},
            'comic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['comics.Comic']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '-1'})
        }
    }

    complete_apps = ['comics']