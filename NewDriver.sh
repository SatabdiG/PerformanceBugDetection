#!/usr/bin/env bash

#DriverForMozilla
counter=0
while [ $counter -lt 5 ]
do
echo "Executing test Suite ..."
python TestSuiteRunner.py
echo "Done executing test suite ... "
echo "Deleting previous Lcov files ... "
./lcovDeleter.sh
echo "Done deleting previous LCov files ..."
echo "Creating data files and counts ... "
python InputModuleNew.py
echo "Done Creating data files and counts ... "
counter=$((counter+1))
done
