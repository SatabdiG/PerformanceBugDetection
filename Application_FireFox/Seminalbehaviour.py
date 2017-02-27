#This file will analyse the Data in the "ParsedFile" for the Current Run for all test cases
#It takes as it's input the run number

import sys
from pymongo import MongoClient
import os

client=MongoClient()
db=client["firefox"]

#Get current Run number
runno=sys.argv[1:]
runno=map(str,runno)
runno=''.join(runno)

#TestCasenames that have "Y" are considered as targets for learning
testcasenames=[]

#Input arrays
url=[]
htmlelem=[]
data=[]
htmlkeys=[]
text=[]
loopinformation=[]

#Inputdic
urldc={}
htmlelemdc={}
datadc={}
htmlkeysdc={}
textdc={}
loopinformationdc={}

#create file location
loc="./ParsedFiles"+"Run"+runno
#Get all the testcase from the database that has "Y"
name="Run"+runno



result=db["Run"+runno].find({"value":"Y"})
for doc in result:
    testcasenames.append(str(doc["testcasename"]))

#Feature database
dbname="feature_Run"+runno

totalpath = os.path.join("./ParsedFiles", "Run" + runno)

for eachtestcase in testcasenames:
    #construct the fullpathname
    fullpathname=os.path.join(totalpath,eachtestcase)
    for eachfil in os.listdir(fullpathname):
        if(".txt" in eachfil):
            if("time" not in eachfil):
                #open all the files and exract the necessary information
                if("url" in eachfil):
                    #extract "url" information
                    urlfil=os.path.join(fullpathname,eachfil)
                    #print(urlfil)
                    urlhandler=open(urlfil, "r")
                    for i in urlhandler.readlines():
                        #add to url array
                        url.append(i.strip("\n"))
                    urldc[eachtestcase]=url
                    urlhandler.close()
                elif("data" in eachfil):
                    #extract "url" information
                    datafil=os.path.join(fullpathname,eachfil)
                    #print(urlfil)
                    datahandler=open(datafil, "r")
                    for i in datahandler.readlines():
                        #add to url array
                        data.append(i.strip("\n"))
                    datadc[eachtestcase]=data
                    datahandler.close()
                elif ("htmlelem" in eachfil):
                    # extract "url" information
                    elem = os.path.join(fullpathname, eachfil)
                    # print(urlfil)
                    htmlhandler = open(elem, "r")
                    for i in htmlhandler.readlines():
                        # add to url array
                        htmlelem.append(i.strip("\n"))
                    htmlelemdc[eachtestcase] = htmlelem
                    htmlhandler.close()
                elif ("text" in eachfil):
                    # extract "url" information
                    textfil = os.path.join(fullpathname, eachfil)
                    # print(urlfil)
                    datahandler = open(textfil, "r")
                    for i in datahandler.readlines():
                        # add to url array
                        text.append(i.strip("\n"))
                    textdc[eachtestcase] = text
                    datahandler.close()
                elif ("htmlkey" in eachfil):
                    # extract "url" information
                    datafil = os.path.join(fullpathname, eachfil)
                    # print(urlfil)
                    datahandler = open(datafil, "r")
                    for i in datahandler.readlines():
                        # add to url array
                        htmlkeys.append(i.strip("\n"))
                    htmlkeysdc[eachtestcase] = htmlkeys
                    datahandler.close()
                elif ("loop" in eachfil):
                    # extract "url" information
                    datafil = os.path.join(fullpathname, eachfil)
                    # print(urlfil)
                    datahandler = open(datafil, "r")
                    for i in datahandler.readlines():
                        # add to url array
                        loopinformation.append(i.strip("\n"))
                    loopinformationdc[eachtestcase] = loopinformation
                    datahandler.close()

    #Get time difference from Mongodb
    cursor=db["Run"+runno].find_one({"testcasename":eachtestcase})["timediff"]
    print(cursor)
    #Make the database feature_runnum entry
    db[dbname].insert_one({"testcasename":eachtestcase, "url":urldc[eachtestcase], "htmlkeys":htmlkeysdc[eachtestcase], "text":textdc[eachtestcase], "htmlelem":htmlelemdc[eachtestcase], "text":textdc[eachtestcase], "loop":loopinformationdc[eachtestcase], "data":datadc[eachtestcase], "rating":cursor})







#close database connection
client.close()