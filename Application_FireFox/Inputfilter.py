#Description: This code takes the run number as the input. And goes through the Testcase files in the ParsedFiles folder for that
#testcase and generates a txt for the entire Run that has names of TC that performed poorly when compared  with the oracle.

import sys
import os
from pymongo import MongoClient
from DataStructures import TestCase

client=MongoClient()
db=client["firefox"]

#Global variable
MagnitudeofDiff=2

#Take the run number as input
runno=sys.argv[1:]
runno=map(str, runno)
runno="".join(runno)
collectionname="Run"+runno
#Generate Run file location
fileloc="./ParsedFiles/Run"+runno

#Dictionaries
#tc:time
timeofautdc={}
timeoforacledc={}

#filepath for testcases in currentrun
filepath=[]
#testcase name for testcases in current run
testcasename=[]

#Get all folders in "fileloc"

for fil in  os.listdir(fileloc):
    filepath.append(os.path.join(fileloc,fil))
    testcasename.append(fil)

#For every location in "filepath" get the time.txt information
for i in filepath:
    if(os.path.isfile(i) == False):
        for ft in os.listdir(i):
            if(os.path.isfile(ft) == True):
                if "time" in ft:
                    timeloc=os.path.join(i, ft)
                    filehandler=open(timeloc, "r")
                    for eachele in filehandler:
                        line = eachele.split(":")
                        timeofaut=line[0]
                        timeoforacle=line[1]
                        testcasenumtmp=i.split("/")
                        testcasenum=testcasenumtmp[len(testcasenumtmp)-1]
                        #make the dictionary entries
                        timeofautdc[testcasenum]=timeofaut
                        timeoforacledc[testcasenum]=timeoforacle

                    filehandler.close()



# compare the timing information in the two dictionaries and filter out ones that took 5 times more time

#create a timefile for each run with the TestCases we need to consider
timefile=open(os.path.join(fileloc, "timefile_Run"+runno+".txt"), "w")

for each in timeofautdc.keys():
    #getoracle time and auttime
    autim=timeofautdc[each]
    ortim=timeoforacledc[each]
    if autim > MagnitudeofDiff*ortim:
        #Make the entry in the timefile for the corresponding run
        if(os.path.isfile(os.path.join(fileloc,each)) == True):
            os.remove(os.path.join(fileloc,each))
        timefile.write(os.path.join(fileloc,each)+":"+"Y")
        timefile.write("\n")
        timediff=float(autim)-float(ortim)
        #make the database entries
        result=db[collectionname].insert_one({"testcasename":each, "timeaut":float(autim), "value":"Y", "timeor":float(ortim)})
    else:
        timefile.write(os.path.join(fileloc, each) + ":" + "N")
        timefile.write("\n")
        # make the database entries
        result = db[collectionname].insert_one({"testcasename": each, "timeaut":float(autim), "value": "N", "timeor":float(ortim)})


timefile.close()
client.close()
