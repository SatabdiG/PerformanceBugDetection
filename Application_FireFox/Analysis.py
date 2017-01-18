#This file generates tese cases in the TestCaseFeatures folder
import sys
import  os
from pymongo import MongoClient
from gene import DNA
from gene import Testcase
import random
import datetime
import math

#Current population - Number of new testcases that need to be generated
populationcount=2
random.seed(datetime.datetime.now())
#take runnumber as input
runno=sys.argv[1:]
runno=map(str, runno)
runno="".join(runno)

#path where new testcase features are constructed
testcasepath="./TestCaseFeatures"

##Make the current run folder in Testcasefeatures
newrun=int(runno)+1
runfol="Run"+str(newrun)

#total path where the testcase of the next run are saved
totalpath=os.path.join(testcasepath, runfol)

if(os.path.isdir(totalpath) == False):
    #Make the directory
    os.mkdir(totalpath)

#Databse Connection
client=MongoClient()
db=client["firefox"]

#variables for genetic algorithm
mutationrate=0.01
population=[]
matingpool=[]

#Total number of testcase to generate
#the newly generated testcases are stored in "totalpath"
## construct the database for testcase in the run
#database has the following structure :

urldc = {}
htmlelemdc = {}
htmlkeydc = {}
textdc = {}
timedc = {}
datadc = {}
testcasename=[]

runpath="Run"+str(runno)
filepath=os.path.join("./ParsedFiles",runpath)


### Phase 1 . Set up #####
for i in os.listdir(filepath):
    pathname=os.path.join(filepath,i)
    if(os.path.isdir(pathname) != False):
        # foreach run i
        url = []
        htmlelem = []
        htmlkey = []
        text = []
        time = []
        data=[]
        #For each testcase
        for ft in os.listdir(pathname):
            folpath=pathname.split("/")
            testcase=folpath[len(folpath)-1]
            runpath=folpath[len(folpath)-2]
            if("url" in ft):
                #contains the url file path
                path=os.path.join(pathname, ft)
                #open the urlfile
                urlhandler=open(path, "r")
                #for each line in urlhandler:
                for lin in urlhandler.readlines():
                    url.append(lin.strip("\n"))
                #Make the dictionary entry
                urldc[testcase]=url
                urlhandler.close()
            elif ("data" in ft):
                # contains the url file path
                path = os.path.join(pathname, ft)
                # open the urlfile
                urlhandler = open(path, "r")
                # for each line in urlhandler:
                for lin in urlhandler.readlines():
                    data.append(lin.strip("\n"))
                # Make the dictionary entry
                datadc[testcase] = data
                urlhandler.close()
            elif ("text" in ft):
                # contains the url file path
                path = os.path.join(pathname, ft)
                # open the urlfile
                urlhandler = open(path, "r")
                # for each line in urlhandler:
                for lin in urlhandler.readlines():
                    text.append(lin.strip("\n"))
                # Make the dictionary entry
                textdc[testcase] = text
                urlhandler.close()
            elif ("htmlelem" in ft):
                # contains the url file path
                path = os.path.join(pathname, ft)
                # open the urlfile
                urlhandler = open(path, "r")
                # for each line in urlhandler:
                for lin in urlhandler.readlines():
                    htmlelem.append(lin.strip("\n"))
                # Make the dictionary entry
                htmlelemdc[testcase] = htmlelem
                urlhandler.close()
            elif ("htmlkey" in ft):
                # contains the url file path
                path = os.path.join(pathname, ft)
                # open the urlfile
                urlhandler = open(path, "r")
                # for each line in urlhandler:
                for lin in urlhandler.readlines():
                    htmlkey.append(lin.strip("\n"))
                # Make the dictionary entry
                htmlkeydc[testcase] = htmlkey
                urlhandler.close()
            elif ("time" in ft):
                # contains the url file path
                path = os.path.join(pathname, ft)
                # open the urlfile
                urlhandler = open(path, "r")
                # for each line in urlhandler:
                for lin in urlhandler.readlines():
                    tim=lin.split(":")
                    tim=tim[len(tim)-1]
                    time.append(lin)
                # Make the dictionary entry
                timedc[testcase] = time
                urlhandler.close()

            #create testcase obj
            testcasename.append(testcase)



for name in testcasename:
    tc=Testcase(urldc[testcase],htmlkeydc[testcase],htmlelemdc[testcase],datadc[testcase],textdc[testcase],timedc[testcase], name)
    #add to populationarray
    population.append(tc)


##### End Setup ####

#2 . Fitness function . Assing fitness based on "Run"@runnum database
dname="Run"+runno
timediffaut={}
cursor=db[dname].find()
totaltime=0
for name in cursor:
    totaltime=totaltime+float(name["timeaut"])
    timediffaut[str(name["testcasename"])]=float(name["timeaut"])-float(name["timeor"])

for i in population:
    #assign fitness
    name=i.name
    fitval=timediffaut[name]/totaltime
    i.setfitness(fitval)


#create mating pool
for i in range(0, len(population)):
    num=int(math.fabs(population[i].fitvalue)*100)
    if(num == 0):
        num+=1
    for j in range(0, num):
        matingpool.append(population[i])


newpopulation=[]
#Reproduction
for i in range(0, populationcount):
    ##Choose two parents randomly
    parenta=matingpool[random.randint(0,len(matingpool)-1)]
    parentb=matingpool[random.randint(0,len(matingpool)-1)]
    child=parenta.crossover(parentb, runno)
    newpopulation.append(child)


count=1
for i in newpopulation:
    testfeaturename="tc_"+str(count)
    featurefil=open(os.path.join(totalpath, testfeaturename), "w+")
    featurefil.write("url="+i.url[0])
    featurefil.write("\n")
    featurefil.write("htmlelem=" + i.htmlelem[0])
    featurefil.write("\n")
    featurefil.write("data=" + i.data[0])
    featurefil.write("\n")
    featurefil.write("htmlkey=" + i.htmlkey[0])
    featurefil.write("\n")
    featurefil.write("text=" + i.text[0])
    featurefil.write("\n")

    featurefil.close()
    count+=1





client.close()
