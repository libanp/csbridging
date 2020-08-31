from django.test import TestCase
from django.urls import resolve
from cv.views import cv_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_cv_page_view(self):
        found = resolve('/cv')
        self.assertEquals(found.func, cv_page)

    def test_uses_cv_template(self):
        response = self.client.get('/cv')
        self.assertTemplateUsed(response, 'cv.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/cv', data={'contact_detail': 'email@something.com'})
        self.assertIn('email@something.com', response.content.decode())
        self.assertTemplateUsed(response, 'cv.html')

