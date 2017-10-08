from django.test import TestCase
from django.core.urlresolvers import reverse
import requests


class TestWeb(TestCase):
    """Test suite for the web front-end."""
    def setUp(self):
        pass

    def test_page_loads(self):
        """Verify the home page loads"""
        resp = requests.get('http://localhost:8000/')
        self.assertEquals(resp.status_code, 200)

    def test_bad_url(self):
        """Verify that an invalid URL returns the 404 page, not an error."""
        resp = requests.get('http://localhost:8000/asdf')
        self.assertEquals(resp.status_code, 200)

    def tearDown(self):
        pass
