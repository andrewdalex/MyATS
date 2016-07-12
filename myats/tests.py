from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from django.contrib.auth.models import User
# Create your tests here.

class LoginTest(TestCase):
    def test_login_failure(self):
        setup_test_environment()
        client = Client()
        response = client.post('/login/', {'username': 'failed', 'password':'login'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response,'Please try again.')

    def test_login_success(self):
        setup_test_environment()
        client = Client()
        response = client.get('/login/')
        self.assertNotContains(response, 'Please try again.')
        self.assertTemplateUsed(response,'login.html')
        user = User.objects.create_user('test_user', password='test_password')
        user.save()
        response = client.post('/login/', {'username': 'test_user','password':'test_password'})
        self.assertEqual(response.status_code,302)

    def test_home_restricted(self):
        setup_test_environment()
        client = Client()
        response = client.get('/home/')
        self.assertEqual(response.status_code, 302)
        user = User.objects.create_user('test_user', password='test_password')
        user.save()
        client.login(username='test_user',password='test_password')
        response = client.get('/home/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        client.logout()
        response = client.get('/home/')
        self.assertEqual(response.status_code,302)
