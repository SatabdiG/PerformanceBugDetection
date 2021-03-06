#Description: This file parses the lcov files generated by Mozilla and creates text files in the DATA folder
#They contain counts of every line that was run with the filename that they belong to
#Input: config.txt. It has locations from where to access the index.html file
#Predecessors: The TestSuite has been Run and lcov files have been generated

from bs4 import BeautifulSoup
import sys
from DataStructures import Stack
from os import listdir
from os.path import isfile, isdir, join
import os

runno=sys.argv[1:]
runno=map(str, runno)
runno="".join(runno)

temfile=runno.split("/")
testcasename=temfile[len(temfile)-2]
runname=temfile[len(temfile)-3]
fileloc=os.path.join("./Data",runname)
print(fileloc)

if(os.path.isdir(fileloc) == False):
    os.mkdir(fileloc)

testcaseloc=os.path.join(fileloc, testcasename)
if(os.path.isdir(testcaseloc) == False):
    os.mkdir(testcaseloc)


#Open config.txt file
ft=open("./config.txt","r+")
#Contains the locations that need to taken into account
locations=[]

#Recursive find all the paths that need to be explored
def recurpathfind(locations):
    paths=[]
    st=Stack()
    st.push(locations[0])
    while st.count > 0:
        currloc = st.pop()
        if(currloc == None):
            break;
        for dir in listdir(currloc):
            if isfile(join(currloc,dir)):
                if(dir == "index.html"):
                    paths.append(join(currloc,dir))
            else:
                 path=join(currloc,dir)
                 st.push(path)

    return paths



for i in ft.readlines():
    if ":" in i:
        temp1=i.split(":")
        locations.append(temp1[1].strip("\n"))


#Result contains all file locations that needs to be parsed

result=recurpathfind(locations)

filenames=[]
for i in range(0, len(result)):
    ftemp=open(result[i],"r+")
    content=ftemp.read()
    currdir=ftemp.name.replace("index.html","",1)
    soup=BeautifulSoup(content,'html.parser')
    for link in soup.find_all('a'):
        hre=link.get('href')
        if("http" not in hre and "index.html" not in hre):
            filenames.append(join(currdir,hre))
    ftemp.close()

count=0

for fil in filenames:
    ft=open(fil,"r+")
    content=ft.read()
    newsoup = BeautifulSoup(content, "html.parser")
    size=len(newsoup.findAll("span",{"class":"lineCov"}))
    if(size>0):
        #Filename
        filN=ft.name
        # Create a new File
        newfilloc=os.path.join(testcaseloc, "count"+str(count)+".txt")
        fDATA=open(newfilloc, "w+")
        fDATA.write("##"+filN)
        fDATA.write("\n")

        for sp in newsoup.findAll("span",{"class":"lineCov"}):
            fDATA.write(sp.text)
            fDATA.write("\n")


        count+=1
        fDATA.close()

ft.close()



