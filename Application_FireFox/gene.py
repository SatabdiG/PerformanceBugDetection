import random
import datetime
import math
from pymongo import MongoClient

clientmin=MongoClient()
db=clientmin["firefox"]

maxnumber=500

class Testcase(object):

    def __init__(self, url, htmlkey, htmlelem,data, text, time,name):
        self.url=url
        self.htmlkey=htmlkey
        self.htmlelem=htmlelem
        self.data=data
        self.text=text
        self.time=time
        self.name=name

    def setfitness(self, value):
        self.fitvalue=value
    #Genetic algorithm Goes here
    def crossover(self, parenta, run):
        #### The learning algorithm would go here
        aurl=self.url
        burl=parenta.url
        #acess "Feature_run" database
        dbname="feature_Run"+run
        counta=db[dbname].count({"testcasename":self.name})
        countb=db[dbname].count({"testcasename":parenta.name})
        if(counta == 1):
            child=Testcase(self.url, self.htmlkey, self.htmlelem, self.data, self.text,self.time, self.name)
            return child
        else:
            child = Testcase(parenta.url, parenta.htmlkey, parenta.htmlelem, parenta.data, parenta.text,parenta.time, parenta.name)
            return child





class DNA(object):

    def __init__(self, url ,htmlkey, htmlelem, data, text, time,name):
        self.gene=Testcase(url, htmlkey, htmlelem, data, text, time,name)

    def getgene(self):
        return self.gene



clientmin.close()