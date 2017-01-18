#!/usr/bin/env bash

#Runs the Front end of the System. Creates Folders in ParsedFile with TestCaseNumber

#take as an arugment the Runnumber
runnumber=$1
echo "current run is: $runnumber"
#construct dir in ParsedFiles
dir="./ParsedFiles/Run$runnumber/"
echo "Current directory is $dir"
#Now get all dirs in in dir variable
for dr in $dir*/ ; do
    echo "The directories are :$dr"
    #pass dr as argument to unittestclassassembler.py
    python unitestclassassembler.py $dr
    python unitestoracle.py $dr
    ./AUTrunner.sh
    ./chromerunner.sh
    python timeextractor.py $dr
    ./lcovDeleter.sh
    echo "Running Input ModuleNew"
    python InputModuleNew.py
    echo "Running File Parser"
    python FileParserMozilla.py $dr
done
