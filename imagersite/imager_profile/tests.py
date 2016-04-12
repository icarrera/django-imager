"""Test ImagerProfile model."""
from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
import factory

from imager_profile.models import ImagerProfile


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User


class UserTestCase(TestCase):

    def setUp(self):
        self.user_1 = UserFactory.create(
            username='bob',
            email='bob@example.com',
        )
        self.user_1.set_password('secret')

        self.user_2 = UserFactory.create(
            username='sally',
            email='sally@example.com',
        )
        self.user_2.set_password('moresecret')

    def test_user_has_profile(self):
        self.assertTrue(self.user_1.profile)

    def test_how_many_profiles(self):
        self.assertEqual(len(ImagerProfile.objects.all()), 2)

    def test_expected_user(self):
        self.assertEqual(self.user_1.username, ImagerProfile.active.all()[0].user.username)

    def test_expected_email(self):
        self.assertEqual(self.user_2.email, ImagerProfile.active.all()[1].user.email)

    def test_add_friends(self):
        bob_pr = self.user_1.profile
        bob_pr.friends.add(self.user_2)
        self.assertEqual(bob_pr.friends.all()[0], self.user_2)
        self.assertEqual(self.user_2.friend_of.all()[0], self.user_1.profile)

    def test_delete_user(self):
        ImagerProfile.active.all()[0].delete()
        self.assertNotIn(self.user_1.profile, ImagerProfile.active.all())

        # use the set password method to hash your password
