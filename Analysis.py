######  Start the Ananlysis Phase ########
#Two input files:
#  1. Application Under Test: OutputFileUnderTest.txt
#  2. Oracle timing : OutputOracle.txt

from gene import DNA
import math
import random
import datetime
import numpy as np


fpappTest=open("OutPutFileUnderTest.txt", "r+")
fooracle=open("OutputOracle.txt", "r+")

def LMS(arr):
    x=[]
    y=[]
    xI=0
    xIsqaure=0
    yI=0
    xIyI=0
    for i in range(0,len(arr)-1):
        tuple=arr[i]
        x.append(tuple[0])
        y.append(tuple[1])
    #finding out sumXI
    for i in x:
        xI+=float(i)
    #Find out Sum XIsquare
    for i in x:
        tempval=float(i)*float(i)
        xIsqaure+=tempval
    #find yI
    for i in y:
        yI+=int(i)
    #find xIyI
    for i in range(0, len(x)):
        tempval=float(x[i])*float(y[i])
        xIyI+=tempval
    a=np.array([[xIsqaure,xI],[xI,len(x)]])
    b=np.array([xIyI,yI])
    xRes=np.linalg.solve(a,b)
    return math.floor(xRes[0]), math.floor(xRes[1])


#Seminal behaviour files
filetripcount=open("filetripcounts", "r+")
filefunctioncallfreq=open("functioncallfreq", "r+")

#Contains the loop frequencies
storearr=[]

#create the trip count array
for lin in filetripcount.readlines():
    temp=lin.split(":")
    temparr=[]
    temparr.append(temp[0])
    temparr.append(temp[2].strip('\n'))
    storearr.append(temparr)

#Pass storearr in LMS
a,b=LMS(storearr)

#Rounding off a is a = 0.0
if(a == 0.0):
    a=1.0


#For Application Under Test
#Contains input of Application Under Test
iparr=[]
dicApp={}
#contains Time of Application under Test
timarr=[]

tmptest1=fpappTest.readlines()

for lin in tmptest1:
    if lin!='':
        templin=lin.split(' ')
        iparr.append(templin[0])
        timarr.append(templin[2].strip('\n'))
        dicApp[templin[0]]=templin[2].strip('\n')



# For Oracle
# Contains input of Oracle
iparrOr = []
dicOr={}
# contains Time of Oracle
timarrOr = []

tmptest1or = fooracle.readlines()
for lin in tmptest1or:
    if lin!='':
        templin = lin.split(' ')
        iparrOr.append(templin[0])
        timarrOr.append(templin[2].strip('\n'))
        dicOr[templin[0]]=templin[2].strip('\n')



##### Setup Code #######

#Generate current population from inputs
population=[]
mutationRate=0.01
matingPool=[]


#Initialize the Population
for i in range(0,len(iparr)):
    tempobj=DNA()
    tempobj.setGene(int(iparr[i]))
    population.append(tempobj)

# Selection Phase

#1. Calculate fitness for every member of the population
fitness={}

for i in range(0, len(population)):
    currmember=population[i]
    #calculate fitness
    timeofApp=float(dicApp[str(currmember.gene)])
    timeofOr=float(dicOr[str(currmember.gene)])
    fitness[currmember.gene]=currmember.fitness(timeofApp,timeofOr)

#build mating pool
for i in range(0, len(population)):
    currmember=population[i]
    num=fitness[currmember.gene]
    if num > 0:
        actual=int(math.ceil(num*100))
        for i in range(0,actual):
            matingPool.append(currmember)


#Reproduction
newpopulation=[]

random.seed(datetime.datetime.now())

for i in range(0, len(population)):
    kid=DNA()
    mutatedKid=DNA()
    parenta=matingPool[random.randint(0,len(matingPool)-1)]
    parentb=matingPool[random.randint(0,len(matingPool)-1)]
    genea=parenta.gene
    geneb=parentb.gene
    kid=parenta.crossover(geneb,a,b)
    mutatedKid=kid.mutate(mutationRate)
    newpopulation.append(mutatedKid)

#print the new population onto a file
inputLocation="inputrandom.txt"

inputnumber=open(inputLocation,'w+')

for i in range(0, len(newpopulation)):
    print(str(newpopulation[i].gene))
    inputnumber.write(str(newpopulation[i].gene))
    inputnumber.write("\n")

inputnumber.close()
