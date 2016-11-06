#!/bin/bash

#About : This is an intiator script. It assumes the gcov and gmon files are already present after compilation
#It spilts the files and creates three files : Call Graph, Function call times, coverage metrics with basic blocks
#with branch coverage
count=0
echo "Running Initiator script"
echo "This script creates function times call"
count=$#
if [ $count = 1 ]; then
 #Display entered program name and continue
 echo $1

 #entered file exists. Generate the output files
 #Gprof files
 gprof -Q -b $1 gmon.out > functiontimes.txt
 gprof -q -b $1 gmon.out > callgraph.txt
 #Gcov files
 echo "Enter filename.c"
 read filename

  #File exists
  #create the coverage file
  gcov -b -a $filename coverstats

 else
 echo "Please enter the program name to continue"
 fi

