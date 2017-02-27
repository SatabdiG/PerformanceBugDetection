import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import time
class TestSearch(unittest.TestCase):
	def setUp(self):
		binary = FirefoxBinary('/home/satabdi/mozilla/bug1250037/with/mozilla-central/obj-x86_64-pc-linux-gnu/dist/bin/firefox')
		browser=webdriver.FirefoxProfile('/home/satabdi/mozilla/bug1250037/with/mozilla-central/obj-x86_64-pc-linux-gnu/tmp/scratch_user')
		self.driver = webdriver.Firefox(firefox_binary=binary,  firefox_profile=browser)
		self.starttime=time.time()

	def tearDown(self):
		self.driver.quit()
		t = time.time() - self.starttime
		print "%s: %.3f" % (self.id(), t)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
unittest.TextTestRunner(verbosity=2).run(suite)
