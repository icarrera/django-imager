# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
from imager_profile.tests import UserFactory
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
        self.user = UserFactory.create(
            username='jaimie',
            email='jaimie@example.com'
        )
        self.user.set_password('stuff')

        self.image = PhotoFactory.create(
        title="image-1",
        user=self.user,
        description="This is a nature shot.",

        )

    def test_photo_has_user(self):
        pass

    def test_user_has_photo(self):
        pass

class AlbumTestCase(TestCase):
    def setUp(self):
        pass

    def test_user_has_album(self):
        pass

    def test_photo_in_album(self):
        pass

    def test_photo_in_multiple_albums(self):
        pass
