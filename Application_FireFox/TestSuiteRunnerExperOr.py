import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import time
class TestSearchChrome(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome(executable_path='/home/satabdi/Downloads/chromedriver')
		self.starttime=time.time()

	def tearDown(self):
		self.driver.quit()

		t = time.time() - self.starttime
		print "%s: %.3f" % (self.id(), t)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSearchChrome)
unittest.TextTestRunner(verbosity=2).run(suite)
