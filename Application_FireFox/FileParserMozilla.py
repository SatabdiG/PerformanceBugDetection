#This File Access all the text files in DATA folder and creates text files in "FILES" directory
#As input it takes the TC num
#Output : Creates two files 1. TC@num_condition.txt TC@num_function.txt
#The file contents as as follows: Header: #@TC@num
#LoopNum:Frequency
#Also create index.txt -> contains the mapping
#linename: linetxt

import os.path
import sys


#
#
# #current testcase --> Obtained from console
# testcasenum=sys.argv[1:]
# testcasenum=map(str, testcasenum)
# testcasenum=''.join(testcasenum)


#Get argument from commandline

#Runno contains the Run number
runno=sys.argv[1:]
runno=map(str,runno)
runno=''.join(runno)

tempstr=runno.split("/")
foldername=tempstr[len(tempstr)-2]

testcasenum=foldername.split("TC")
testcasenum=testcasenum[len(testcasenum)-1]

#parsedfileloc="./ParsedFiles"
parsedfileloc=runno
filloc="./Data"
#Contains the location for all files in the Data Folder
filelocs=[]


for fil in os.listdir(filloc):
    tmp=os.path.join(filloc, fil)
    filelocs.append(tmp)

#For each file in the filelocs:
#1. Open the file
#2. Search for "if" and "else"
#3. Create the mappingfile TC@numLoopMapping.txt
#4. The mapping file has the entry -->linenum  --- line to which it is allocated to
#3. Create a file TC@numloop.txt in parsedfileloc
#4. TC@numloop.txt has data like ---> linenum --> frequency

ifcounter=[]
elsecounter=[]
filenumdict={}
#Contain the mapping
linenumdict={}



#create the TC@nummap in ParsedFiles --> MApping file
filwrite=open(os.path.join(parsedfileloc, testcasenum+"map.txt"), "w+")

#Create the TC@num_Loop.txt
tcwrite=open(os.path.join(parsedfileloc, testcasenum+"_loop.txt"), "w+")

count=0
for fil in filelocs:
    #Open the file
    filhand=open(fil, "r+")

    for i in filhand.readlines():
        if(i!=""):
            temp=i.strip(' ').split(":")
            if("#" not in temp[0]):
                if(str(temp[1]).find("for", 0,10)>0):
                    #temmp[1] -->line temp[0] --> frequency
                    print(temp[1] +"  "+ temp[0])
                    filwrite.write(str(count)+":"+temp[1])
                    filwrite.write("\n")
                    tcwrite.write(str(count)+":"+temp[0])
                    tcwrite.write("\n")
                    filenumdict[temp[1]]=temp[0]
                    count=count+1


    #i --:> line ### filenumdict[i] --> frequency of line



    #Close the open file
    filhand.close()


filwrite.close()
tcwrite.close()