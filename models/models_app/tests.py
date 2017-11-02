from datetime import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


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


class CreateLotteryTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.lottery_data = {
            'title': 'sample_lottery',
            'description': 'this is a test lottery',
            'participants': '',
            'start_time': datetime.now(),
            'end_time': datetime.now(),
            'date_created': datetime.now()
        }
        self.response = self.client.post(
            reverse('create'),
            self.lottery_data,
            format='json')

    def test_api_can_create_a_lottery(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


class CreateBidTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.bid_data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'username': 'test_jsmith2017',
            'birthday': datetime.now()
        }
        self.response = self.client.post(
            reverse('create'),
            self.bid_data,
            format='json')

    def test_api_can_create_a_bid(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


class CreateGameTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.game_data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'username': 'test_jsmith2017',
            'birthday': datetime.now()
        }
        self.response = self.client.post(
            reverse('create'),
            self.game_data,
            format='json')

    def test_api_can_create_a_game(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


class CreateCardTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.card_data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'username': 'test_jsmith2017',
            'birthday': datetime.now()
        }
        self.response = self.client.post(
            reverse('create'),
            self.card_data,
            format='json')

    def test_api_can_create_a_card(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
