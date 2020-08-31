from django.test import TestCase
from django.urls import resolve
from cv.views import cv_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_cv_page_view(self):
        found = resolve('/cv')
        self.assertEquals(found.func, cv_page)

    def test_uses_home_template(self):
        response = self.client.get('/cv')
        self.assertTemplateUsed(response, 'cv.html')

