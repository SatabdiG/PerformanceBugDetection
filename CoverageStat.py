#This script opens the OutPutFileUnderTest.txt file. Selects the inputs that have the input "y"
# Creates a folder for each selected input.
# Then onward to generating the coverage characteristics with gcov
# Remove the gcda file and excute code for all selected inputs.
# Move the generated files to destination folder.

#Destination folder


import  os.path
import shutil

des="./Results/appTest/CoverageStats"
cummugcdaloc="./Results/Runs"
filename="customBS.gcda"
fileApp="customBS.c"
fileName="customBS"
fileGCda=fileName+".c.gcov"
inputdat=[]

#openfile
fpopen=open("OutPutFileUnderTest.txt", "r+")

for line in fpopen.readlines():
    templin=line.split(" ")
    print(templin[3])
    if(templin[3].strip() == "Y"):
        inputdat.append(templin[0])


for i in range(0,len(inputdat)):
    #Remove the file to "Runs" the .gcda file is it exists as the results are cummalative
    if os.path.isfile(filename):
        os.remove(filename)


    #execute the filename with the inputs in inputdat
    os.system("./custom "+inputdat[i])
    os.system("gcov -b " + fileApp)

    #Create new directory based on input and move the new gcov files there
    if not os.path.exists(os.path.join(des,inputdat[i])):
        os.mkdir(os.path.join(des,inputdat[i]))

    newpath=os.path.join(des,inputdat[i])
    #Make Sure the new place is empty
    if os.path.isfile(os.path.join(newpath,fileName+".c.gcov")):
        os.remove(os.path.join(newpath,fileName+".c.gcov"))
    shutil.move(fileName+".c.gcov",newpath)


#close opened files
fpopen.close()
