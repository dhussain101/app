from django.test import TestCase
import requests


class GetLotteriesTestCase(TestCase):
    """Tests suite for the main lottery exp API."""
    def setUp(self):
        pass  # nothing to set up

    def test_success_response(self):
        """Verify communication between exp API and entity layer."""
        response = requests.get('http://localhost:8001/lotteries')
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        pass  # nothing to tear down


class GetCardsTestCase(TestCase):
    """Tests suite for the main card exp API."""
    def setUp(self):
        pass  # nothing to set up

    def test_success_response(self):
        """Verify communication between exp API and entity layer."""
        response = requests.get('http://localhost:8001/cards')
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        pass  # nothing to tear down


class GetLotteryDetailsTestCase(TestCase):
    """Tests suite for the main lottery detail exp API."""
    def setUp(self):
        pass  # nothing to set up

    def test_success_response(self):
        """Verify communication between exp API and entity layer."""
        response = requests.get('http://localhost:8001/lotteries/1')
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        pass  # nothing to tear down


class GetCardDetailsTestCase(TestCase):
    """Tests suite for the main card detail exp API."""
    def setUp(self):
        pass  # nothing to set up

    def test_success_response(self):
        """Verify communication between exp API and entity layer."""
        response = requests.get('http://localhost:8001/cards/1')
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        pass  # nothing to tear down
