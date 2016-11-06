## This script goes through the seminal coverage file generated for each input and creates the predictive models for each input
## and stores them in a file in the same location. --> The predictive model should be y=ax+b
# For now using Least squares
# For behaviours we consider --> Loop Counts, function calls frequencies, function times


import os.path
import re
#get location of coverage file for each input
location="./Results/appTest/CoverageStats"
filename='customBS.c.gcov'

inputname=[]
totallocations=[]
loopcounts={}
temparr=[]
viewedlinenum=[]
storelocation=[]

#Main array for Loop Counts
functionobjs=[]
#Main array contains the function calls and names
functioncalls=[]
functionnames=[]


#Get the functionline
class StoreObjfunc(object):
    def __init__(self, selfcount, linenum,input):
        self.functioncount=selfcount
        self.linenum=linenum
        self.input=input

#Get function call frequency

class functionsumm(object):
    def __init__(self, functionname, count,input):
        self.functionname=functionname
        self.count=count
        self.input=input

#get all folders in the path
for file in os.listdir(location):
    inputname.append(file)
    totallocations.append(os.path.join(location,file))


#for each input, open corresponding folder, get the gCov file
for i in range(0, len(inputname)):
    ft=open(os.path.join(totallocations[i],filename), 'r+')
    viewedlinenum=[]
    functionnames=[]
    #for each
    for line in ft.readlines():
       if ':' in line:
           temparr=line.split(':')
           tripcount=temparr[0].strip()
           linenum=temparr[1].strip()
           codeline=temparr[2].strip()
           #Check if code line contains either ["for", "while", "do"]
           if(codeline.startswith("while") or codeline.startswith("for") or codeline.startswith("do")):
               if linenum not in viewedlinenum:
                   viewedlinenum.append(linenum)
                   #create the linum obj
                   tempboj=StoreObjfunc(tripcount,linenum,inputname[i])
                   functionobjs.append(tempboj)

       if 'function' in line:
           templin=line.split(" ")
           funcname=templin[1].strip()
           timecalled=templin[3].strip()
           if(funcname not in functionnames):
               functionnames.append(funcname)
               objtmp=functionsumm(funcname,timecalled,inputname[i])
               functioncalls.append(objtmp)



    #Close the opened file
    ft.close()

#Create  one files for each folder -> 1.tripcount
#inp linenum functioncount

filetrip=open("filetripcounts", "w+")
functioncallfreq=open("functioncallfreq", "w+")

for i in functionobjs:
    filetrip.write(i.input+":"+i.linenum+":"+i.functioncount)
    filetrip.write("\n")


for i in functioncalls:
    functioncallfreq.write(i.input+":"+i.functionname+":"+i.count)
    functioncallfreq.write("\n")

#Close open file
filetrip.close()
functioncallfreq.close()













