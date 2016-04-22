"""Test ImagerProfile model."""
from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
import factory

from imager_profile.models import ImagerProfile


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User


class UnsavedUserCase(TestCase):
    """Test if user is not saved to database."""
    def setUp(self):
        self.user_0 = UserFactory.build(
            username='george',
            email='george@example.com'
        )
        self.user_0.set_password('secret')

    def test_unsaved_user(self):
        """Unsaved user should not have a user id."""
        self.assertIsNone(self.user_0.id)

    def test_create_user_profile(self):
        """Test saving user creates a user profile."""
        george_pr = ImagerProfile(user=self.user_0)
        self.assertIs(george_pr, self.user_0.profile)

class ExistingUserCase(TestCase):
    """Test if user exists."""

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
        """Test if use has a profile."""
        self.assertTrue(self.user_1.profile is not None)

    def test_how_many_profiles(self):
        """Test number of expected Imager profiles."""
        self.assertEqual(len(ImagerProfile.objects.all()), 2)

    def test_user_active(self):
        """Test if user's profile is active."""
        self.assertTrue(self.user_1.profile in ImagerProfile.active.all())

    def test_profile_has_pk(self):
        """Test if profile has a primary key."""
        self.assertTrue(self.user_2.profile.pk)

    def test_expected_user_username(self):
        """Test username is as expected."""
        self.assertEqual(self.user_1.username, 'bob')

    def test_expected_email(self):
        """Test user email is as expected."""
        self.assertEqual(self.user_2.email, 'sally@example.com')

    def test_str(self):
        """Test ImagerProfile string method."""
        sally_pr = self.user_2.profile
        self.assertEquals(str(sally_pr), 'sally')

    def test_add_friends(self):
        """Test adding friends to a profile."""
        bob_pr = self.user_1.profile
        bob_pr.friends.add(self.user_2)
        self.assertEqual(bob_pr.friends.all()[0], self.user_2)
        self.assertEqual(self.user_2.friend_of.all()[0], self.user_1.profile)

    def test_not_friends(self):
        """Test that a user is not a friend of another profile."""
        sally_pr = self.user_2.profile
        self.assertNotIn(self.user_1.profile, sally_pr.friends.all())

    def test_delete_user(self):
        """Test deleted user no longer has an Imager profile."""
        self.user_1.delete()
        self.assertNotIn(self.user_1.profile, ImagerProfile.objects.all())

    def test_no_profile_pk_after_delete(self):
        """Test that deleted user does not have a profile primary key."""
        self.user_1.delete()
        self.assertIsNone(self.user_1.profile.pk)
