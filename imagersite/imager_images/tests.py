# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from imager_profile.tests import UserFactory
import factory

from imager_images.models import Photo, Album

class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo

    image = factory.django.ImageField(color='blue')

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
        self.image_3 = PhotoFactory.create(
            title="image 3",
            user=self.user,
            description="This is a portrait of a cat.",
        )
        self.album_1 = AlbumFactory.create(
            title='2016',
            user=self.user
        )

        self.album_2 = AlbumFactory.create(
            title='Outdoor Adventures',
            user=self.user
        )
        self.image_1.albums.add(self.album_1)
        self.image_2.albums.add(self.album_1)
        self.image_1.albums.add(self.album_2)

    def test_album_exists(self):
        """Test album was created."""
        self.assertIsInstance(self.album_1, Album)

    def test_photo_exists(self):
        """Test photo was created."""
        self.assertIsInstance(self.image_1, Photo)

    def test_photo_in_album(self):
        """Test if photo is in an album."""
        self.assertIn(self.image_2, self.album_1.photos.all())

    def test_photo_in_multiple_albums(self):
        """Test if photo is in two separate albums."""
        self.assertIn(self.image_1, self.album_1.photos.all())
        self.assertIn(self.image_1, self.album_2.photos.all())

    def test_photo_not_in_album(self):
        """Test that photo was not added to album."""
        self.assertNotIn(self.image_3, self.album_1.photos.all())

    def test_user_has_photo(self):
        """Test that user associated with photo is as expected."""
        self.assertEqual(self.user, self.image_1.user)

    def test_user_has_album(self):
        """Test that user associated with album is as expected."""
        self.assertEqual(self.user, self.album_1.user)

    def test_album_has_multiple_photos(self):
        """Test number of photos in album is as expected."""
        self.assertEqual(len(self.album_1.photos.all()), 2)
