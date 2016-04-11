# -*-coding: utf-8 -*-
"""Imager image classes."""
from django.db import models
from django.conf import settings

PRIVACY_SETTINGS = [
    ('private', 'private'),
    ('shared', 'shared'),
    ('public', 'public')
]


class Photo(models.Model):
    """Individual picture uploaded by a user."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(null=True, blank=True)
    published = models.CharField(max_length=255,
                                 choices=PRIVACY_SETTINGS,
                                 default='private')


class Album(models.Model):
    """Photos and meta-data about the photos."""

    pass
