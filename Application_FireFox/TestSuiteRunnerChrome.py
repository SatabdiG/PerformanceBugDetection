#Runs the test suite for the oracle

import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import os

class PythonOrgChrome(unittest.TestCase):
    def setUp(self):
        #chromedriver = "/usr/bin/google-chrome"
        #os.environ["webdriver.chrome.driver"] = chromedriver
        #self.driver=webdriver.Chrome(chromedriver)
        #self.driver = webdriver.Chrome(executable_path='/usr/bin/google-chrome')
        self.driver=webdriver.Chrome(executable_path='/home/satabdi/Downloads/chromedriver')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def test_serach(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("abcd")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source



    def tearDown(self):
        self.driver.close()


suite = unittest.TestLoader().loadTestsFromTestCase(PythonOrgChrome)
unittest.TextTestRunner(verbosity=2).run(suite)