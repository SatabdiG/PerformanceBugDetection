#Create Graphs

import matplotlib.pyplot as plt
import os.path
import numpy as np


fileName="customBS"
fileGCda=fileName+".c.gcov"
fileGCdaLoc="./Results/Runs"
#Colors for Lines
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
for i in range(len(tableau20)):
    r, g, b = tableau20[i]
    tableau20[i] = (r / 255., g / 255., b / 255.)

#Take OutputOracle File and OutPutFileUnderTest File and create graphs from them

#OutPutFileUndertest

fOpen=open("OutPutFileUnderTest.txt","r+")

fAppInput=[]
fAPPTime=[]

#Format the Input File
for i in fOpen.readlines():
    temp=i.split(" ")
    fAppInput.append(int(temp[0]))
    fAPPTime.append(float(temp[2].strip("\n")))


#Enter the Oracle Information

fOpenOr=open("OutputOracle.txt", "r+")
fAppInputOr=[]
fAPPTimeOr=[]
for i in fOpenOr.readlines():
    temp=i.split(" ")
    fAppInputOr.append(int(temp[0]))
    fAPPTimeOr.append(float(temp[2].strip("\n")))


#Plot the Graph

nPFAPPInput=np.asarray(fAppInput)
nPAPPTime=np.asarray(fAPPTime)

nPFAPPInputOr=np.asarray(fAppInputOr)
nPAPPTimeOr=np.asarray(fAPPTimeOr)

fig=plt.figure(figsize=(12, 14))

ainp=plt.subplot(211)

ainp.set_title("Application Under Test")
ainp.set_ylabel("Time MS")
plt.plot(nPFAPPInput,nPAPPTime,"g^")

aOr=plt.subplot(212)

aOr.set_title("Oracle vs App under Test")
aOr.set_xlabel("Input")
aOr.set_ylabel("Time Ms")

fig.add_subplot(ainp)
fig.add_subplot(aOr)

ax=plt.gca()
plt.plot(nPFAPPInputOr,nPAPPTimeOr,'bs',label="Oracle" );
plt.plot(nPFAPPInput,nPAPPTime,"g^", label="Application Under Test");
plt.legend(numpoints=1,loc="upper right")
plt.grid(True)

#save the Graphs
fig.savefig("Graph.png")

#From the Compiled GCDA file create the html file.
fgcov=open(os.path.join(fileGCdaLoc,fileGCda), "r+")
#Result html file
fRes=open("combinedGcda.html", "w+")

fRes.write( """<html>
<head>
<title>Coverage Data </title>
</head>
<body style="background-color: powderblue;">
<h1> <center> Program Summary </center></h1>
</break>
</break>
""")
for dat in fgcov.readlines():
    temp=dat.split(":")
    linecount=temp[0].strip()
    if "-" not in linecount:
        if linecount == "#####":
           fRes.write("""<div style="color:blue">%s</div><break>""" %(dat))
        else:
            if "function" in linecount:
               fRes.write("""<div style="color:powderpink">%s</div><break>""" % (dat))
            else:
                if "call" in linecount:
                    fRes.write("""<div style="color:powderpink">%s</div><break>""" % (dat))
                else:
                    if "branch" in linecount:
                        fRes.write("""<div style="color:powderpink">%s</div><break>""" % (dat))
                    else:
                        if int(linecount)>=0:
                            fRes.write("""<div style="color:#F15230">%s</div><break>""" % (dat))
    else:
        print >> fRes, """<div ">%s</div><break>""" % (dat)



fRes.write("""</body></html>""")

#Close the Open file
fOpen.close()
fOpenOr.close()
fgcov.close()
fRes.close()