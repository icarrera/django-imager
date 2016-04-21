# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 03:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0002_auto_20160412_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='camera_model',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='friend_of', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='photography_type',
            field=models.CharField(blank=True, choices=[('portrait', 'Portrait Photography'), ('nature', 'Nature Photography'), ('sports', 'Sports Photography')], max_length=255, null=True),
        ),
    ]