import unittest
from selenium import webdriver
import time

# este test debe ser ejecutado perfectamente por selenium
class TestAddPoliticalParty(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS()

        
        
    def test_signup_fire(self):
        #Realizamos login, con las credenciales a continuacion

        self.driver.set_window_size(1120, 550)
        self.driver.get("https://duckduckgo.com/")
        self.driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
        self.driver.find_element_by_id("search_button_homepage").click()
        print('si selenium')

        

    def tearDown(self):
        self.driver.quit

if __name__ == '__main__':
    unittest.main()

