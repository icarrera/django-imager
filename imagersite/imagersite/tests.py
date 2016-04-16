from django.core import mail
from django.test import TestCase, Client
from django.test.client import RequestFactory
from imager_profile.tests import UserFactory
from django.contrib.auth.views import login

class SimpleTest(TestCase):
    def setUp(self):
        self.r_factory = RequestFactory()
        self.user_1 = UserFactory.create(
            username='jaimie',
            email='jaimie@example.com'
        )
        self.user_1.set_password('stuff12345')
        self.user_2 = UserFactory.build(
            username='krampus',
            email='krampus@krampus.net'
        )
        self.user_2.set_password('krampusrocks')
        self.cl = Client()

    def test_get_bad_uri(self):
        """Test 404 Error for invalid uri."""
        response = self.cl.get('/l0g!n/')
        self.assertEqual(response.status_code, 404)

    def test_login_view_get(self):
        """Test 200 status code response for login view."""
        response = self.cl.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_view_authentication(self):
        response = self.cl.post('/login/', {'username': self.user_1.username, 'password': self.user_1.password})
        pass

    def test_login_post(self):
        self.cl.login(username=self.user_1, password=self.user_1.password)
        pass

    def test_register_view_get(self):
        """Test 200 status code response for register view."""
        response = self.cl.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)


class EmailTest(TestCase):
    def test_send_email(self):
        mail.send_mail('yo yo yo', 'hey sup?',
                       'magic@magic.com', ['stuff@where.com'],
                       fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
