import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import time
class TestSearch(unittest.TestCase):
	def setUp(self):
		binary = FirefoxBinary('/home/satabdi/mozilla-central/obj-x86_64-pc-linux-gnu/dist/bin/firefox')
		browser=webdriver.FirefoxProfile('/home/satabdi/mozilla-central/obj-x86_64-pc-linux-gnu/tmp/scratch_user')
		self.driver = webdriver.Firefox(firefox_binary=binary,  firefox_profile=browser)
		self.starttime=time.time()
	def test_0(self):
		driver = self.driver
		driver.get("http://realfavicongenerator.net/")
		self.assertIn("Favicon", driver.title)
		elem = driver.find_element_by_name("site")
		elem.send_keys("google.com")
		elem.send_keys(Keys.RETURN)
		assert "No results found." not in driver.page_source
	def test_1(self):
		driver = self.driver
		driver.get("http://cgi.ebay.com.au/INDIGO-MOON-BEADED-DEVORE-JACKET-BNWT-SIZE-M_W0QQitemZ110004721071QQihZ001QQcategoryZ53367QQrdZ1QQcmdZViewItem")
		self.assertIn("Python", driver.title)
		elem = driver.find_element_by_name("_nkw")
		elem.send_keys("pycon")
		elem.send_keys(Keys.RETURN)
		assert "No results found." not in driver.page_source
	def test_2(self):
		driver = self.driver
		driver.get("https://www.google.de")
		self.assertIn("google", driver.title)
		elem = driver.find_element_by_name("q")
		elem.send_keys("google.comftgyhhui,")
		elem.send_keys(Keys.RETURN)
		assert "No results found." not in driver.page_source
	def test_3(self):
		driver = self.driver
		driver.get("http://www.python.org")
		self.assertIn("Python", driver.title)
		elem = driver.find_element_by_name("q")
		elem.send_keys("abcd")
		elem.send_keys(Keys.RETURN)
		assert "No results found." not in driver.page_source

	def tearDown(self):
		self.driver.quit()
		t = time.time() - self.starttime
		print "%s: %.3f" % (self.id(), t)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
unittest.TextTestRunner(verbosity=2).run(suite)
