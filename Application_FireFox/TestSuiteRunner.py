#Description:This executes a predefined testsuite in the ./TestSuiteFolder
#Predecessor:Runs first. Keeps track of time and input for each run
#After: A shell script needs to delete the lcov file and run the coverage report again

### Make Sure that Nightly is the currently active browser from setting
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class PythonOrgSerach(unittest.TestCase):
    def setUp(self):
        binary = FirefoxBinary('/home/satabdi/mozilla-central/obj-x86_64-pc-linux-gnu/dist/bin/firefox')
        self.driver = webdriver.Firefox(firefox_binary=binary)

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


"""
if __name__ == "__main__":
    unittest.main()
"""

suite = unittest.TestLoader().loadTestsFromTestCase(PythonOrgSerach)
unittest.TextTestRunner(verbosity=2).run(suite)

"""
binary = FirefoxBinary('/home/tasu/Mozilla/mozilla-central/obj-x86_64-pc-linux-gnu/dist/bin/firefox')
driver = webdriver.Firefox(firefox_binary=binary)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
"""