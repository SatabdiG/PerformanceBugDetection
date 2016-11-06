"""
Input Module :
Generates a population of n rnadom numbers(input)

"""

from gene import DNA


maxpopulationsize=50
matingpool=[]
referencediff=50

inputLocation="inputrandom.txt"

inputnumber=open(inputLocation,'w+')

#statup

#Array of DNA elements
population=[]
#poplate the population array with Random numbers
for i in range(0,maxpopulationsize):
    temp=DNA()
    #write to a file:
    inputnumber.write(str(temp.gene))
    inputnumber.write("\n")
    population.append(temp)


inputnumber.close()


