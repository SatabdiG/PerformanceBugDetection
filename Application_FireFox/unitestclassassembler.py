#Name:unitesteclassassembler
#version:1.0
#description:Accesses all the txt files from the TestCase module and constructs the TestSuiteRunner.py

import os.path
import sys

#filepathname
filename=[]
filepath=[]


#Get argument from commandline

#Runno contains the Run number
runno=sys.argv[1:]
runno=map(str,runno)
runno=''.join(runno)

tempstr=runno.split("/")
foldername=tempstr[len(tempstr)-2]

testcasenum=foldername.split("TC")
testcasenum=testcasenum[len(testcasenum)-1]


loc="./TestCase"
writefile=os.path.join("./", "TestSuiteRunnerExper.py")

writehandle=open(writefile, "w+")


for file in os.listdir(loc):
    if testcasenum in file:
        filename.append(file)
        locs=os.path.join(loc, file)
        filepath.append(locs)

count=0

# Set up import libraries
writehandle.write("import unittest")
writehandle.write("\n")
writehandle.write("from selenium import webdriver")
writehandle.write("\n")
writehandle.write("from selenium.webdriver.firefox.firefox_binary import FirefoxBinary")
writehandle.write("\n")
writehandle.write("from selenium.webdriver.common.keys import Keys")
writehandle.write("\n")
writehandle.write("import time")
writehandle.write("\n")


#Set Up class structure

writehandle.write("class TestSearch(unittest.TestCase):")
writehandle.write("\n")
writehandle.write("\t" + "def setUp(self):")
writehandle.write("\n")
writehandle.write("\t\t" + "binary = FirefoxBinary('/home/tasu/Mozilla/mozilla-central/obj-x86_64-pc-linux-gnu/dist/bin/firefox')")
writehandle.write("\n")
writehandle.write("\t\t" + "self.driver = webdriver.Firefox(firefox_binary=binary)")
writehandle.write("\n")
writehandle.write("\t\t" + "self.starttime=time.time()")
writehandle.write("\n")

#for every testcase in the folder
for fil in filepath:
    opfile=open(fil, "r+")
    writehandle.write("\tdef " + "test_" + str(count) + "(self):")
    writehandle.write("\n")
    for i in opfile.readlines():
        if(i != ""):
            writehandle.write("\t\t"+i)
    count+=1



    opfile.close()

#setup teardown code

writehandle.write("\n")
writehandle.write("\t" + "def tearDown(self):")
writehandle.write("\n")
writehandle.write("\t\t" + "self.driver.quit()")
writehandle.write("\n")
writehandle.write("\t\t" + "t = time.time() - self.starttime")
writehandle.write("\n")
writehandle.write("\t\t" + 'print "%s: %.3f" % (self.id(), t)')
writehandle.write("\n")
writehandle.write("\n")

writehandle.write("suite = unittest.TestLoader().loadTestsFromTestCase(TestSearch)")
writehandle.write("\n")
writehandle.write("unittest.TextTestRunner(verbosity=2).run(suite)")
writehandle.write("\n")


writehandle.close()
