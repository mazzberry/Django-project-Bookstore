from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class SignUpTest(TestCase):

    def test_signup_url_byname(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)


    def test_signup_url_byurl(self):
        response = self.client.get('/accounts/signup')
        self.assertEqual(response.status_code, 200)



