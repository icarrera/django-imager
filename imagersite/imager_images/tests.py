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
    """Test cases for the Photo and Album classes."""

    def setUp(self):
        """Setup of users, photos, and albums for tests."""
        self.user = UserFactory.create(
            username='jaimie',
            email='jaimie@example.com'
        )
        self.user.set_password('stuff123')

        self.sad_user = UserFactory.create(
            username='sadnope',
            email='sadnope@example.com'
        )
        self.sad_user.set_password('meh123123')

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
            description='Random photos 2016.',
            user=self.user
        )

        self.album_2 = AlbumFactory.create(
            title='Outdoor Adventures',
            description='PNW travel photos.',
            user=self.user
        )
        self.image_1.albums.add(self.album_1)
        self.image_2.albums.add(self.album_1)
        self.image_1.albums.add(self.album_2)

    def test_photo_exists(self):
        """Test photo was created."""
        self.assertIsInstance(self.image_1, Photo)

    def test_photo_title(self):
        """Test photo title is as expected."""
        self.assertEqual(self.image_1.title, 'image 1')

    def test_photo_description(self):
        """Test photo description is as expected."""
        self.assertEqual(self.image_1.description, 'This is a nature shot.')

    def test_photo_date_uploaded(self):
        """Test that the photo uploaded has a datetime stamp."""
        self.assertIsNotNone(self.image_1.date_uploaded)

    def test_photo_in_album(self):
        """Test if photo is in an album."""
        self.assertIn(self.image_2, self.album_1.photos.all())

    def test_photo_in_multiple_albums(self):
        """Test that photo is in two separate albums."""
        self.assertIn(self.image_1, self.album_1.photos.all())
        self.assertIn(self.image_1, self.album_2.photos.all())

    def test_photo_not_in_album(self):
        """Test that photo was not added to album."""
        self.assertNotIn(self.image_3, self.album_1.photos.all())

    def test_photo_delete(self):
        """Test that deleted photo is no longer in album."""
        self.image_1.delete()
        self.assertNotIn(self.image_1, self.album_1.photos.all())

    def test_user_has_photo(self):
        """Test that user associated with photo is as expected."""
        self.assertEqual(self.user, self.image_1.user)

    def test_user_does_not_own_photo(self):
        """Test that a user is not associated with a particular photo."""
        self.assertNotEqual(self.sad_user, self.image_1.user)

    def test_user_has_album(self):
        """Test that a user associated with album is as expected."""
        self.assertEqual(self.user, self.album_1.user)

    def test_user_does_not_own_album(self):
        """Test that a user is not associated with a particular album."""
        self.assertNotEqual(self.sad_user, self.album_1.user)

    def test_album_exists(self):
        """Test album was created."""
        self.assertIsInstance(self.album_1, Album)

    def test_album_title(self):
        """Test album title is as expected."""
        self.assertEqual(self.album_1.title, '2016')

    def test_album_description(self):
        """Test album description is as expected."""
        self.assertEqual(self.album_1.description, 'Random photos 2016.')

    def test_album_privacy(self):
        """Test album privacy settings default to private."""
        self.assertEqual(self.album_1.published, 'private')

    def test_album_date_uploaded(self):
        """Test that the album uploaded has a datetime stamp."""
        self.assertIsNotNone(self.album_1.date_uploaded)

    def test_album_has_multiple_photos(self):
        """Test number of photos in album is as expected."""
        self.assertEqual(len(self.album_1.photos.all()), 2)
