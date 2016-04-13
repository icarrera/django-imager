# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 14:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imager_images', '0004_auto_20160413_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='photo_files/%Y-%m-%d')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_published', models.DateTimeField(blank=True, null=True)),
                ('published', models.CharField(choices=[('private', 'private'), ('shared', 'shared'), ('public', 'public')], default='private', max_length=255)),
                ('photos', models.ManyToManyField(related_name='photos', to='imager_images.Album')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
