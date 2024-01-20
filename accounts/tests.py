from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.

class SignUpTest(TestCase):
    username = 'myUsername'
    email = 'myEmail736@gmail.com'

    def test_signup_url_byname(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)


    def test_signup_url_byurl(self):
        response = self.client.get('/accounts/signup')
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        #get_user_model() #user modeli ke dakhel project hast ra be ma mide (farghe ba import kardan model:hich moghe jash tagir nemikone)
        userModel = get_user_model()
        user = userModel.objects.create_user(
            self.username,
            self.email,
            )
        self.assertEqual(userModel.objects.all().count(), 1)
        # self.assertEqual(userModel.objects.all()[0], self.username)
        # self.assertEqual(userModel.objects.all()[1], self.email)


