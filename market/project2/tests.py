from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from datetime import datetime

# Create your tests here.


class CreatePersonTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.person_data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'username': 'test_jsmith2017',
            'birthday': datetime.now()
        }
        self.response = self.client.post(
            reverse('create'),
            self.person_data,
            format='json')

    def test_api_can_create_a_person(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
