# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 20:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0005_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='photos',
            new_name='albums',
        ),
    ]
