#This Script browses through all folders in ./Results/appTest/CoverageStats and creates block table
#Also some visualization of the functioncall structure and time taken for the function


import os.path

des="./Results/appTest/CoverageStats"

filename="customBS.c.gcov"
filenames=[]
filedestinations=[]
blocks=[]
blockName={}
count=0
jusarray=[]

for file in os.listdir(des):
    filenames.append(file)
    filedestinations.append(os.path.join(des,file))

#Open Each coverage Block generate Block Table
for fil  in range(0, len(filenames)):
    ft=open(os.path.join(filedestinations[fil], filename),"r+")
    ### Main Parser Code ####
    for i in ft.readlines():
        jusarray.append((i.strip("\n")))
    for i in range(0, len(jusarray)):
        temparr = []
        if(":" not in jusarray[i]):
            print(jusarray[i])
            #Encountered block end

            for j in range(0,i-1):
                print(jusarray[i])
                #temparr.append(jusarray[j])
            #blockName[count]=temparr
            #count+=1








#Close Each opened filed
ft.close()