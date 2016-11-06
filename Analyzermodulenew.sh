#!/bin/bash
count=0
while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "Text read from file: $line"
    echo "Doing Something"
    { time ./customBS.o $line ; } &> ./Results/appTest/"Run$count.txt"
     gprof -Q -b customBS.o gmon.out > ./Results/appTest/FunctionCalls/"functiontimes$count.txt"
     gprof -q -b customBS.o gmon.out > ./Results/appTest/Callgraphs/"callgraph$count.txt"
     gcov -b customBS.c
    count=$((count+1))
    echo $count
done < "$1"