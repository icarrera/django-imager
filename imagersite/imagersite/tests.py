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
        self.user_1.save()
        self.user_2 = UserFactory.build(
            username='krampus',
            email='krampus@krampus.net'
        )
        self.user_2.set_password('krampusrocks')
        self.cl = Client()

    def test_get_bad_uri(self):
        """Test 404 Error for invalid uri."""
        response = self.cl.get('/accounts/l0g!n/')
        self.assertEqual(response.status_code, 404)

    def test_login_view_get(self):
        """Test 200 status code response for login view."""
        response = self.cl.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, 'registration/login.html')

    def test_login_view_authentication(self):
        """Test if valid user is able to login."""
        logged_in = self.cl.login(username='jaimie', password='stuff12345')
        self.assertTrue(logged_in)

    def test_login_fail(self):
        """Test invalid user login failure."""
        logged_in = self.cl.login(username='krampus', password='krampusrocks')
        self.assertFalse(logged_in)

    def test_logout_view_get(self):
        """ Test 200 status code response for logout view."""
        response = self.cl.get('/accounts/logout/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, 'registration/logout.html')

    def test_register_view_get(self):
        """Test 200 status code response for register view."""
        response = self.cl.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, 'registration/registration_form.html')

    def test_registration_complete_view(self):
        response = self.cl.get('/accounts/register/complete/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, 'registration/registration_complete.html')

    def test_activation_complete_view(self):
        response = self.cl.get('/accounts/activate/complete/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, 'registration/activation_complete.html')


class EmailTest(TestCase):
    def test_send_email(self):
        mail.send_mail('yo yo yo', 'hey sup?',
                       'magic@magic.com', ['stuff@where.com'],
                       fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
