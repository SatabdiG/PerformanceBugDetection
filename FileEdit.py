#File Editor
#Descriptor:
#Arrange the input to produce outputs for the Analysis file
#Produces Two Text Files
#Textfile 1: Test Application: I/p Time : The value is chosen for the next population Y or N
#Textfile 2: Oracle Application : I/p Time :

#Location of OutofRuns for Application under test

import os.path

#Globalvariable that decides that keeps the margin of how much the testinput time needs to be greater than the input time for the
#oracle to be considered
greaterthan=3

loc1="./Results/appTest"
loc2="./Results/Oracle"

applicationunderTestNames=[]
applicationunderTestLocations=[]
oracleNames=[]
oracleLocations=[]

#create the Input Array
inparray=[]
ifile=open("inputrandom.txt","r+");
for li in ifile.readlines():
    inparray.append(int(li.strip("\n")))


#Get name and locations for the Application Under Test files
for name in os.listdir(loc1):
    if os.path.isfile(os.path.join(loc1,name)):
        applicationunderTestNames.append(name)
        applicationunderTestLocations.append(os.path.join(loc1,name))


#Get name and location for the Oracle files

for name in os.listdir(loc2):
    if os.path.isfile(os.path.join(loc2,name)):
        oracleNames.append(name)
        oracleLocations.append(os.path.join(loc2,name))


#Create Two Files
fpAppTest=open("OutPutFileUnderTest.txt", "w+")
fpOracle=open("OutputOracle.txt", "w+")

timmingapp=[]

########## Writing to Application ubder test file ###################
#For each file
for i in range(0,len(applicationunderTestLocations)):
    temp=open(applicationunderTestLocations[i], "r+")
    temptiming=open(applicationunderTestLocations[i], "r+")
    #for each file in each file
    # first line will have the input
    #temparr=temp.readlines()[0].split(' ')[3].strip('\n')
    #inputarrayapp.append(temparr)
    #timing information will begin with a "real word"
    for lin in temptiming.readlines():
        if lin!=' ':
            if "real" in lin:
                temptime=lin.split('\t')[1].strip('\n').strip('s').split('m')
                mins=temptime[0]
                secs=temptime[1]
                minstosecs=float(mins)*60+float(secs)
                timmingapp.append(minstosecs)



############ End of Application under test writing #####################
########## Writing to Oracle file ######################

timmingor=[]

for i in range(0,len(oracleLocations)):
    tempor=open(oracleLocations[i], "r+")
    temptimingor=open(oracleLocations[i], "r+")
    #for each file in each file
    # first line will have the input
    #temparr=tempor.readlines()[0].split(' ')[3].strip('\n')
    #inputarrayor.append(temparr)
    #timing information will begin with a "real word"
    for lin in temptimingor.readlines():
        if "real" in lin:
            temptime=lin.split('\t')[1].strip('\n').strip('s').split('m')
            mins=temptime[0]
            secs=temptime[1]
            minstosecs=float(mins)*60+float(secs)
            timmingor.append(minstosecs)
            break


# write to file

for i in range(0, len(inparray)):
     if (float(timmingapp[i])*1000 - float(timmingor[i]*1000)>= 5):
            fpAppTest.write(str(inparray[i]) + "  " + str(timmingapp[i])+" "+"Y")
            fpAppTest.write("\n")
     else:
         fpAppTest.write(str(inparray[i]) + "  " + str(timmingapp[i]) + " " + "N")
         fpAppTest.write("\n")

#write to file
for i in range(0, len(inparray)):
    fpOracle.write(str(inparray[i])+"  "+str(timmingor[i]))
    fpOracle.write("\n")

########### End of oracle File Writing Phase ##########################


#Close the Two open files
fpAppTest.close()
fpOracle.close()
temp.close()
temptiming.close()
#tempor.close()
#temptimingor.close()