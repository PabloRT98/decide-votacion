import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

class TestSignup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def test_signup_fire(self):
        self.driver.get("http://localhost:8000/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("aguza")
        self.driver.find_element_by_id('id_password').send_keys("aguzaaguza")
        time.sleep(2)
        self.driver.find_element_by_css_selector('div.submit-row').click()

        time.sleep(1)
        self.driver.find_element_by_link_text("Votings").click()

    def tearDown(self):
        self.driver.quit

if __name__ == '__main__':
    unittest.main()