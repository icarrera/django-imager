# -*-coding: utf-8 -*-
"""Imager image classes."""
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

PRIVACY_SETTINGS = [
    ('private', 'private'),
    ('shared', 'shared'),
    ('public', 'public')
]


@python_2_unicode_compatible
class Photo(models.Model):
    """Individual picture uploaded by a user."""

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False
    )
    photos = models.ManyToManyField(Album, related_name='photos')
    image = models.ImageField(upload_to='photo_files/%Y-%m-%d', null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(null=True, blank=True)
    published = models.CharField(
        max_length=255,
        choices=PRIVACY_SETTINGS,
        default='private'
    )

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Album(models.Model):
    """Photo Album and meta-data about the photos."""

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='albums',
        null=False
    )
    cover = models.ForeignKey(
        Photo,
        related_name='cover_photo',
        blank=True
    )
    title = models.CharFireld(max_length=255)
    description = models.TextField(blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    published = models.CharField(
        max_length=255,
        choices=PRIVACY_SETTINGS,
        default='private'
    )


    def __str__(self):
        return self.title
