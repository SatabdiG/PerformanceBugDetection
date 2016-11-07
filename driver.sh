#!/bin/bash
counter=0

#This Script Drives the Entire Project
python InputModule.py
while [ $counter -lt 5 ]
do
echo "---- Running Run Number --- $counter"
#Run Runner Module
echo "Running module for Application under Test"
./Analyzermodulenew.sh inputrandom.txt
echo "Running module for Oracle"
./AnalyzerModuleOracleNew.sh inputrandom.txt
echo "Finished The Runner Module"
echo "Starting the Analysis module"
python FileEdit.py
echo "Finished File Edit"
python CoverageStat.py
echo "Finished creating coverage Files"
python SeminalBehaviour.py
echo "Finished Creating the Seminal behaviour files"
python Analysis.py
echo "Finished Analysis"
python Visualization.py
echo "Finished creating the graph"	
python Evaluation.py $counter
echo "Moved Files"
#python BlkTimeGenerator.py $counter
#echo "Created Blk Time Output Files"
counter=$((counter+1))
done

