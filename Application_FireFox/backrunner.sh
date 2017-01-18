#!/usr/bin/env bash

#Takes the run number as input and runs Analysis section of code
#take as an arugment the Runnumber
runnumber=$1
echo "Current Run number is $runnumber"
echo "Running Inputfilter ... "
python Inputfilter.py $runnumber
echo "Done running Input filter ..."
echo "Running Seminal Behaviour script ... "
python Seminalbehaviour.py $runnumber
echo "Done running Seminal Behaviour script ..."
echo "Running analysis"
python Analysis.py $runnumber
echo "Done running analysis.py"