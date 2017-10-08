from django.test import TestCase, Client


class GetLotteriesTestCase(TestCase):
    def setUp(self):
        pass  # nothing to set up

    def test_success_response(self):
        response = self.client.get('http://models-api:8000/lotteries')
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        pass  # nothing to tear down


class GetCardsTestCase(TestCase):
    def setUp(self):
        pass  # nothing to set up

    def test_success_response(self):
        response = self.client.get('http://models-api:8000/cards')
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        pass  # nothing to tear down


class GetLotteryDetailsTestCase(TestCase):
    def setUp(self):
        pass  # nothing to set up

    def test_success_response(self):
        response = self.client.get('http://models-api:8000/lotteries/1')
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        pass  # nothing to tear down


class GetCardDetailsTestCase(TestCase):
    def setUp(self):
        pass  # nothing to set up

    def test_success_response(self):
        response = self.client.get('http://models-api:8000/cards/1')
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        pass  # nothing to tear down
