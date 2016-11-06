#Move the Two OutputFiles to RunFolder

import sys
import os.path
import shutil

runno=sys.argv[1:]
runno=map(str,runno)
runno=''.join(runno)

fileName="customBS"
fileGCda=fileName+".c.gcov"

fileGCdaLoc="./Results/Runs"
srcfilelocApp="OutPutFileUnderTest.txt"
srcfilelocOr="OutputOracle.txt"
srcGraph="Graph.png"
srcfilHTML="combinedGcda.html"
directory="./Results/Runs/"+runno
if not os.path.exists(directory):
    os.makedirs(directory)

shutil.copy(srcfilelocApp,directory)
shutil.copy(srcfilelocOr,directory)
shutil.copy(srcGraph,directory)
#Move the GCDA file
if os.path.isfile(os.path.join(fileGCdaLoc,fileGCda)):
    os.remove(os.path.join(fileGCdaLoc,fileGCda))
shutil.move(os.path.join(fileGCdaLoc,fileGCda),directory)
shutil.move(srcfilHTML, directory)
