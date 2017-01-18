#Description : This file runs at the beginning of each Run. It is application specific. It takes the features in the "Feature"
# folder and creates the testcases in the "TestCase" folder based on a specific template.
#The template file is : testcasetemplate.txt
#The feature set from which to populate the testcase folder is in "TestCaseFeature"
#It then sets up the Folderstructure in "Parsed Files" folder. It creates a folder with the name of the current Run. Then for each testcase
#It creates documents : url.txt, HTML elements.txt (Feature structutes)

import os
import sys

## Global variables & file paths
par="./ParsedFiles"

#The file that conatins the testcase template
#testcasetemplate=open("testcasetemplate.txt", "r+")


#Runno contains the Run number
runno=sys.argv[1:]
runno=map(str,runno)
runno=''.join(runno)

#filename to be created in Parsedfiles for the current Run
currfolname="Run"+runno

#Contains the features from the learning module
runnum="Run"+runno
testcasefeatures=os.path.join("./TestCaseFeatures",runnum)

#create folder structure in Parsed files
## Create the Run folder in ParsedFiles
if(os.path.isdir(os.path.join(par, currfolname)) == False):
    os.mkdir(os.path.join(par,currfolname))

newrunloc=os.path.join(par,currfolname)



mapdiction={'url':[], 'htmlelem':[], 'data':[], 'text':[]}
url=[]
html=[]
data=[]
text=[]
htmlkey=[]

count=0

#for each files in the "TestCaseFeatures" folder create a seperate testcase based on template : "testcasetemplate.txt"
for fil in os.listdir(testcasefeatures):
    ftestfea=open(os.path.join(testcasefeatures, fil), "r")
    mapdiction = {'url': [], 'htmlelem': [], 'data': [], 'text': [], 'htmlkey':[]}
    for eachlin in ftestfea.readlines():
        lisele=eachlin.split("=")
        dataname=lisele[0]
        value=lisele[1]
        if(dataname == "url"):
            url.append(value.strip("\n"))
        elif(dataname == "htmlelem"):
            html.append(value.strip("\n"))
        elif(dataname == "data"):
            data.append(value.strip("\n"))
        elif(dataname == "text"):
            text.append(value.strip("\n"))
        elif (dataname == "htmlkey"):
            val=value.strip("\n")
            val=val.strip('"')
            htmlkey.append(val)

    #Update the dictionary
    mapdiction["url"]=url
    mapdiction["htmlelem"]=html
    mapdiction["data"] = data
    mapdiction["text"] = text
    mapdiction["htmlkey"] = htmlkey
    ftestfea.close()
    count+=1

newcount=0

for i in range(0,count):
    testcasetemplate = open("testcasetemplate.txt", "r+")
    # create a new file for each fil
    filname = "tc_" + str(i) + ".txt"
    testcasefile = open(os.path.join("./TestCase", filname), "w+")
    testcasefile.write("driver = self.driver")
    testcasefile.write("\n")
    # Files that need to created in the Run folder
    newfolname="TC"+str(i)
    newtemp=os.path.join(newrunloc,newfolname)
    if(os.path.isdir(newtemp) == False):
        os.mkdir(newtemp)

    urlfil = open(os.path.join(newtemp, "url.txt"), "w")
    htmlfil = open(os.path.join(newtemp, "htmlelem.txt"), "w")
    text= open(os.path.join(newtemp, "text.txt"), "w")
    htmlkey=open(os.path.join(newtemp, "htmlkey.txt"), "w")
    data=open(os.path.join(newtemp, "data.txt"), "w")

    #Create testcase based on mapdiction entry
    for readline in testcasetemplate.readlines():
        newstr=""
        if "url" in readline:
            urlfil.write(mapdiction["url"][newcount])
            urlfil.write("\n")
            newstr=readline.replace("url",mapdiction["url"][newcount])
        elif "htmlelem" in readline:
            htmlfil.write(mapdiction["htmlelem"][newcount])
            htmlfil.write("\n")
            newstr=readline.replace("htmlelem",mapdiction["htmlelem"][newcount])
        elif "data" in readline:
            data.write(mapdiction["data"][newcount])
            data.write("\n")
            newstr=readline.replace("data",mapdiction["data"][newcount])
        elif "text" in readline:
            text.write(mapdiction["text"][newcount])
            text.write("\n")
            newstr=readline.replace("text",mapdiction["text"][newcount])
        elif "htmlkey" in readline:
            htmlkey.write(mapdiction["htmlkey"][newcount])
            htmlkey.write("\n")
            newstr=readline.replace("htmlkey",mapdiction["htmlkey"][newcount])
        #write new str into the newly created testcase file
        testcasefile.write(newstr)
        #testcasefile.write("\n")
    testcasefile.write('assert "No results found." not in driver.page_source')
    testcasefile.write("\n")
    testcasefile.close()
    testcasetemplate.close()
    urlfil.close()
    htmlfil.close()
    htmlkey.close()
    text.close()
    data.close()
    newcount+=1





