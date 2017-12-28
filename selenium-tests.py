from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME)

class FrontEndTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome()
        super(FrontEndTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(FrontEndTestCase, self).tearDown()

    def test_home(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/')
        assert 'For all your card-collecting needs' in selenium.page_source

    def test_lotteries(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/lotteries')
        assert 'lottery-list' in selenium.page_source

    def test_cards(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/cards')
        assert 'card-list' in selenium.page_source

    def test_login(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/cards')

        username = selenium.find_element_by_id('id_username')
        password = selenium.find_element_by_id('id_password')
        submit = selenium.find_element_by_tag_name('button')

        username.send_keys('alice1')
        password.send_keys('12345678')
        submit.send_keys(Keys.RETURN)

        assert 'Welcome, Alice' in selenium.page_source

    def test_register(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/cards')

        first_name = selenium.find_element_by_id('id_first_name')
        last_name = selenium.find_element_by_id('id_last_name')
        username = selenium.find_element_by_id('id_username')
        password = selenium.find_element_by_id('id_password')
        confirm_password = selenium.find_element_by_id('id_confirm_password')
        birthday = selenium.find_element_by_id('id_birthday')
        submit = selenium.find_element_by_tag_name('button')

        first_name.send_keys('Jane')
        last_name.send_keys('Doe')
        username.send_keys('jane1')
        password.send_keys('87654321')
        confirm_password.send_keys('87654321')
        birthday.send_keys('12/23/96')
        submit.send_keys(Keys.RETURN)

        assert 'Welcome, Jane' in selenium.page_source
