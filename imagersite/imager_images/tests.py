# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
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

        self.image_1 = PhotoFactory.create(
            title="image 1",
            user=self.user,
            description="This is a nature shot.",
        )
        self.image_2 = PhotoFactory.create(
            title="image 2",
            user=self.user,
            description="This is a sports photo.",
        )
        self.album_1 = AlbumFactory.create(
            title='2016',
            user=self.user
        )

        self.album_2 = AlbumFactory.create(
            title='Outdoor Adventures',
            user=self.user
        )

    def test_album_exists(self):
        """Test album was created."""
        self.assertIsInstance(self.album_1, Album)

    def test_photo_exists(self):
        """Test photo was created."""
        self.assertIsInstance(self.image_1, Photo)

    # def test_photo_has_user(self):
    #     pass
    #
    # def test_user_has_photo(self):
    #     pass
    #
    # def test_user_has_album(self):
    #     pass
    #
    # def test_photo_in_album(self):
    #     pass
    #
    # def test_photo_in_multiple_albums(self):
    #     pass
