from django.core import mail
from django.test import TestCase, Client
from django.test.client import RequestFactory
from imager_profile.tests import UserFactory
from imager_images.tests import PhotoFactory, AlbumFactory
from django.contrib.auth.views import login

class ViewsTest(TestCase):
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
        self.cl_2 = Client()
        self.cl_3 = Client()
        self.user_3 = UserFactory.create(
            username='hacker',
            email='hacker@hacker.com',
        )
        self.user_3.set_password('iwilltrytohackyou')
        self.user_3.save()
        self.image_1 = PhotoFactory.create(
            title="image 1",
            user=self.user_1,
            description="This is a nature shot.",
        )
        self.image_2 = PhotoFactory.create(
            title="image 2",
            user=self.user_3,
            description="This is a sports photo.",
            published='public',
        )
        self.album_1 = AlbumFactory.create(
            title='2016',
            description='Random photos 2016.',
            user=self.user_1,
            cover_photo=self.image_1
        )
        self.album_2 = AlbumFactory.create(
            title='sports',
            description='This is sporty.',
            user=self.user_3,
            cover_photo=self.image_2
        )
        self.album_1.pictures.add(self.image_1)
        self.album_2.pictures.add(self.image_2)

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
        """Test 200 status code for registration complete view."""
        response = self.cl.get('/accounts/register/complete/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, 'registration/registration_complete.html')

    def test_activation_complete_view(self):
        """Test 200 status code for activation complete view."""
        response = self.cl.get('/accounts/activate/complete/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, 'registration/activation_complete.html')

    def test_library_view(self):
        """Test 200 status code for library view."""
        response = self.cl.get('/images/library/')
        self.assertEqual(response.status_code, 302)

    def test_view_own_library(self):
        logged_in = self.cl.login(username='jaimie', password='stuff12345')
        response = self.cl.get('/images/library/')
        response_body = response.content.decode('utf-8')
        self.assertIn(
            'images/photos/' + str(self.image_1.id),
            response_body
        )

    def test_permission_denied(self):
        logged_in = self.cl.login(username='jaimie', password='stuff12345')
        logged_in2 = self.cl_3.login(username='hacker', password='iwilltrytohackyou')
        photo_id = self.image_1.id
        response = self.cl_3.get('/images/photos/' + str(photo_id))
        self.assertEqual(response.status_code, 403)

    def test_view_libraries_different(self):
        logged_in = self.cl_3.login(username='hacker', password='iwilltrytohackyou')
        response = self.cl_3.get('/images/library/')
        response_body = response.content.decode('utf-8')
        self.assertNotIn(
            'images/photos/' + str(self.image_1.id),
            response_body
        )

    def test_user_view_public_photo(self):
        logged_in = self.cl.login(username='jaimie', password='stuff12345')
        photo_id = self.image_2.id
        response = self.cl.get('/images/photos/' + str(photo_id))
        self.assertEqual(response.status_code, 200)




class EmailTest(TestCase):
    def test_send_email(self):
        mail.send_mail('yo yo yo', 'hey sup?',
                       'magic@magic.com', ['stuff@where.com'],
                       fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
