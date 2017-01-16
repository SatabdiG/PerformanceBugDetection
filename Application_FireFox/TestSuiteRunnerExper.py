import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import time
class TestSearch(unittest.TestCase):
	def setUp(self):
		binary = FirefoxBinary('/home/tasu/Mozilla/mozilla-central/obj-x86_64-pc-linux-gnu/dist/bin/firefox')
		self.driver = webdriver.Firefox(firefox_binary=binary)
		self.starttime=time.time()
	def test_0(self):
		driver = self.driver
		driver.get("http://www.python.org")
		self.assertIn("Python", driver.title)
		elem = driver.find_element_by_name("q")
		elem.send_keys("pycon")
		elem.send_keys(Keys.RETURN)
		assert "No results found." not in driver.page_source

	def tearDown(self):
		self.driver.quit()
		t = time.time() - self.starttime
		print "%s: %.3f" % (self.id(), t)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
unittest.TextTestRunner(verbosity=2).run(suite)
