# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0003_remove_album_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='photos',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='user',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
