#description : Take the current run as input. For the current run go into the folder /Run@num. Get the testcases that have "Y" from
#mongodb. and The test cases that take "N" in mongo db.  If a block of code of a testcase with "Y" is in a testcase count "N"
#remove the block of code. Prepare a document that has the common blocks of code for the test cases that have a "Y" in them.

import sys
import os
from pymongo import MongoClient

#Contains the Run number
runno=sys.argv[1:]
runno=map(str,runno)
runno=''.join(runno)

fileloc="./Data/Run"+runno

#make a mongodb connection get all the testcases that have "Y" in them
client=MongoClient()
db=client["firefox"]

testcases=db["Run"+runno].find({"value":"Y"})

mattertc=[]

for each in testcases:
    mattertc.append(str(each["testcasename"]))


alltestcases=[]
testcasespath=[]

for alldir in os.listdir(fileloc):
    alltestcases.append(alldir)
    testcasespath.append(os.path.join(fileloc, alldir))

othertc=[]

reqtc=[]

for path in range(0, len(testcasespath)):
    currtestcase=alltestcases[path]
    if(currtestcase not in mattertc):
        #Enter Folder
        folname=os.path.join(testcasespath[path])
        #Open "Folname"
        othertc.append(folname)
    else:
        folname = os.path.join(testcasespath[path])
        reqtc.append(folname)

fileblock={}
testcaseblock={}

for tc in reqtc:
    for files in os.listdir(tc):
        ft=open(os.path.join(tc,files), "r+")
        for lin in ft.readlines():
            for each in othertc:
                #open the directory
                    for eachfil in os.listdir(each):
                        blocks = []
                        totalname=os.path.join(each, eachfil)
                        #open the files:
                        filname=open(totalname, "r+")
                        totallines=filname.readlines()
                        if(lin not in totallines):
                            blocks.append(lin)
                        filname.close()
                        fileblock[eachfil]=blocks
    testcaseblock[tc]=fileblock


    ft.close()


filterblock=[]
folpath="./Blocks/Run"+runno
if(os.path.isdir(folpath) == False):
    os.mkdir(folpath)
for eachval in mattertc:
    #createfolder with matter testcase
    folpath=os.path.join(folpath, eachval)
    if(os.path.isdir(folpath) == False):
        os.mkdir(folpath)
    filname=os.path.join(folpath,eachval)+".txt"
    writefil=open(filname, "w")
    #get the corresponding entry from testcaseblock
    key="./Data/Run"+runno+"/"+eachval
    result=testcaseblock[key]
    for keys in result:
        writefil.write(keys)
        writefil.write("\n")
        strval=result[keys]
        for lin in strval:
            writefil.write(lin)
            writefil.write("\n")
    writefil.close()

client.close()


