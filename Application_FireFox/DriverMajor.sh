#!/usr/bin/env bash
#Runs the front module and backmodule
counter=0
while [ $counter -lt 5 ]
do
echo "In Run $counter"
python assembler.py $counter
./FrontModule.sh $counter
./backrunner.sh  $counter
counter=$((counter+1))
done