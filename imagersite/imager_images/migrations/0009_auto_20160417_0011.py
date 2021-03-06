# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 00:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0008_auto_20160414_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='cover_photo',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='cover', to='imager_images.Album'),
        ),
        migrations.AlterField(
            model_name='album',
            name='pictures',
            field=models.ManyToManyField(related_name='photos', to='imager_images.Photo'),
        ),
    ]
