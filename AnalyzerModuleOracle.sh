#!/bin/bash
count=0
while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "Text read from file: $line"
    echo "Doing Something"
    { time ./pin -t trace.so  -o ./Results/Oracle/Traces/"Trace$count.txt" -- ./bs.o $line ; } &> ./Results/Oracle/"Run$count.txt"    
    count=$((count+1))
    echo $count			
done < "$1"	        
