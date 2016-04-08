from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
import factory

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User


class UserTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create(
            username='bob',
            email='bob@blahblah.com',
        )
        self.user.set_password("secret")

    def test_foo(self):
        pass

        # never create a user and just put the password in
        # use the set password method to hash your password
