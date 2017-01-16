#!/usr/bin/env bash

#DriverForMozilla
counter=0
while [ $counter -lt 5 ]
do
#echo "Executing test Suite ..."
#python TestSuiteRunner.py
#python TestSuiteRunnerChrome.py
#echo "Done executing test suite ... "
#echo "Deleting previous Lcov files ... "
#./lcovDeleter.sh
#echo "Done deleting previous LCov files ..."
#echo "Creating data files and counts ... "
#python InputModuleNew.py
#echo "Done Creating data files and counts ... "
#python FileParserMozilla.py
#echo "Done Parsing files"
echo "Running Assembler"
python assembler.py $counter
./FrontModule.sh $counter
counter=$((counter+1))
done
