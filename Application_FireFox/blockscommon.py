#description:Take the runnumber as input and generate the common code block summary.

import os
import sys
from pymongo import MongoClient

#Contains the Run number
runno=sys.argv[1:]
runno=map(str,runno)
runno=''.join(runno)

blockpath="./Blocks/Run"+runno

client=MongoClient()
db=client["firefox"]


testcases=db["Run"+runno].find({"value":"Y"})

mattertc=[]
pathnames=[]

for each in testcases:
    mattertc.append(str(each["testcasename"]))
    pathnames.append(os.path.join(blockpath, str(each["testcasename"])))

blocks={}

for eachval in pathnames:
    for eachfil in os.listdir(eachval):
        folname=os.path.join(eachval, eachfil)
        reader=open(folname, "r+")
        blocks[eachfil.strip(".txt")]=reader.readlines()
        reader.close()
j=0
filnaleblocks={}



client.close()