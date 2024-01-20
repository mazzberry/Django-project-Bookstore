from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class HomePageTest(TestCase):
    def test_home_page_url_byname(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'yeah it\'s home')

    def test_home_page_logint_exists(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'login')

    def test_home_page_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_template_used(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

