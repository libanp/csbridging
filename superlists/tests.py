from django.test import TestCase
from django.urls import resolve
from superlists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/superlists')
        self.assertEquals(found.func, home_page)
