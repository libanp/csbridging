from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from superlists.views import home_page

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/superlists')
        self.assertTemplateUsed(response, 'home.html')
