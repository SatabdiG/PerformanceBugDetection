import random
import datetime
import math

maxnumber=500


class DNA(object):

    def __init__(self):
        random.seed(datetime.datetime.now())
        self.gene=random.randint(0,maxnumber)

    def setGene(self, number):
        self.gene=number

    #By How much percentage is the timeAPP greater than timeOr
    def fitness(self, timeApp, timeOr):
        diff=timeApp-timeOr
        rateofdiff=diff/timeApp
        return rateofdiff

        # Val value of
    def RetVal(self, a1, b, val):
            # y=0
            # y=a*x+b
            y = a1 * val + b
            return y

    def crossover(self, partnergene,a,b):
        child=[]
        owngene=self.gene
        partg=partnergene
        #diff=math.fabs(owngene-partg)

        newchild1=a*owngene+b
        newchild12=a*partg+b
        #print(str(newchild1)+"  "+str(newchild12))
        diff=math.fabs(newchild1-newchild12)
        owngeneStr = str(newchild1)
        partgStr = str(newchild12)

        #pad with zeros in case one is less than the other
        if(len(owngeneStr)>len(partgStr)):
            diff=len(owngeneStr)-len(partgStr)
            tempdiff=diff+len(partgStr)
            for i in range(len(partgStr), len(owngeneStr)):
                partgStr+="0"
        else:
            if (len(partgStr) > len(owngeneStr)):
                for i in range(len(owngeneStr), len(partgStr)):
                    owngeneStr+="0"

        midpoint=random.randint(0,len(owngeneStr))

        for i in range(0, len(owngeneStr)):
            if(i > midpoint):
                child.append(owngeneStr[i])
            else:
                if(i >= len(partgStr)):
                    child.append(0)
                else:
                    child.append(partgStr[i])


        stemo=map(str,child)
        stemo=''.join(stemo)
        if stemo.count('.') > 1:
            tmps=stemo.split(".")
            stemo=tmps[0]

        kid=DNA()
        somenum=random.random()
        if(somenum<0.3):
            stemo = math.fabs(float(stemo) + diff)

        else:
            stemo = math.fabs(float(stemo) - diff)

        stemo=math.ceil(float(stemo))
        print(stemo)
        kid.setGene(int(stemo))
        return kid

    def mutate(self, mutationRate ):
        kidgene=self.gene
        kidgeneStr=str(kidgene)
        newgene=[]
        for i in range(0, len(kidgeneStr)):

            somenum=random.random()
            if(somenum < mutationRate):
                #mutate current num

                temnum=str(random.randint(0,9))
                newgene.append(temnum)
            else:
                newgene.append(kidgeneStr[i])


        mapNum=map(str, newgene)
        mapNum=''.join(mapNum)
        newKid=DNA()
        newKid.setGene(int(mapNum))
        return newKid


