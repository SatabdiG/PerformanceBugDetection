#Description:This executes a predefined testsuite in the ./TestSuiteFolder
#Predecessor:Runs first. Keeps track of time and input for each run
#After: A shell script needs to delete the lcov file and run the coverage report again

### Make Sure that Nightly is the currently active browser from setting

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ldtp import *
import os.path
from ldtputils import *
from subprocess import call
import threading
import time


class  NightlyRunner(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print "Starting " + self.name
        call(["/home/tasu/Mozilla/mozilla-central/mach", "run"])
        print "Exiting " + self.name

class RunSuite(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name

    def run(self):
        print("Starting" + self.name)
        time.sleep(5)
        print(ldtp.getwindowlist())



print("Before Threads")
print(ldtp.getwindowlist())
# Create new threads
thread1 = NightlyRunner(1, "Thread-1")
thread2=RunSuite(2, "TestSuiteRunner")


# Start new Threads
thread1.start()
thread2.start()

print "Exiting Main Thread"


#print(ldtp.getwindowlist())

#Firefoxlocation="/home/tasu/Mozilla/mozilla-central/obj-x86_64-pc-linux-gnu/dist/bin"
#MachRunlocation="/home/tasu/Mozilla/mozilla-central/mach run"

#call(["/home/tasu/Mozilla/mozilla-central/mach", "run"])

#print("Getting windows list"+ldtp.getwindowlist())





"""
from twill.commands import *

go("http://www.google.com/")
showforms()
fv("1","q","Say what")
submit("btnI")

show()
"""


"""
driver=webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
"""