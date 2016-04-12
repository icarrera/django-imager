# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
import factory

from imager_images.models import Photo, Album

class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album


class PhotoTestCase(TestCase):
    def setUp(self):
        pass

class AlbumTestCase(TestCase):
    def setup(self):
        pass
