from django.test import TestCase, Client


class GetLotteriesTestCase(TestCase):
    """Tests suite for the main lottery exp API."""
    def setUp(self):
        pass  # nothing to set up

    def test_success_response(self):
        """Verify communication between exp API and entity layer."""
        response = self.client.get('http://models-api:8000/lotteries')
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        pass  # nothing to tear down


class GetCardsTestCase(TestCase):
    """Tests suite for the main card exp API."""
    def setUp(self):
        pass  # nothing to set up

    def test_success_response(self):
        """Verify communication between exp API and entity layer."""
        response = self.client.get('http://models-api:8000/cards')
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        pass  # nothing to tear down


class GetLotteryDetailsTestCase(TestCase):
    """Tests suite for the main lottery detail exp API."""
    def setUp(self):
        pass  # nothing to set up

    def test_success_response(self):
        """Verify communication between exp API and entity layer."""
        response = self.client.get('http://models-api:8000/lotteries/1')
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        pass  # nothing to tear down


class GetCardDetailsTestCase(TestCase):
    """Tests suite for the main card detail exp API."""
    def setUp(self):
        pass  # nothing to set up

    def test_success_response(self):
        """Verify communication between exp API and entity layer."""
        response = self.client.get('http://models-api:8000/cards/1')
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        pass  # nothing to tear down
