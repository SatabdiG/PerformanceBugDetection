#Description: This creates the time information for each testcase in "Parsed File" specific Run
# This runs after both AUTrunner and chromerunner have finished.
#It takes as an input "timeaut.txt" and "timechrome.txt"
import os
import sys

#Runno contains the Run number
runno=sys.argv[1:]
runno=map(str,runno)
runno=''.join(runno)

pathname=os.path.join("./ParsedFiles/Run"+runno)


#Timeinfo for AUT :
#dictionary of the format "testcasename":"time"
autinfo={}
#Timeinfo for AUT :
chromeinfo={}


autfil=open("timeaut.txt", "r+")
chromefil=open("timechrome.txt", "r+")

for eachlin in autfil.readlines():
    if( ":" in eachlin):
        temp=eachlin.split(":")
        val=temp[1]
        tst=temp[0].split(".")
        name=tst[len(tst)-1]
        #make an entry in the dictionary
        autinfo[name]=float(val.strip("\n"))


for eachlin in chromefil.readlines():
    if( ":" in eachlin):
        temp=eachlin.split(":")
        val=temp[1]
        tst=temp[0].split(".")
        name=tst[len(tst)-1]
        #make an entry in the dictionary
        chromeinfo[name]=float(val.strip("\n"))

count=0
for key in autinfo.keys():
    #create a file in location
    temploc=os.path.join(pathname, "TC"+str(count))
    timefil=open(os.path.join(temploc,"time.txt"),"w")
    timefil.write(str(autinfo[key])+":"+str(chromeinfo[key]))
    timefil.close()
    count+=1

autfil.close()
chromefil.close()


