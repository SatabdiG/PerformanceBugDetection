
## Performance Bug Analysis and Detetction

**Introduction** 

The Project tries to find out performance bugs, areas in code that give poor performance by comparing with another oracle. It uses Seminal Behaviour, genetic algorithm and Learning techniques to generate new inputs for which the program takes a longer time exposing areas of the code that take longer for the given input.

The Source Code is composed of a series of Python Scripts that execute one after the other. The *driver.sh* contains all the information and executes the python script in order.

1. Assumptions : Source Code is available for Application under Test. Source code is not required for Oracle. 
2. The initial input file is provided in either a file or added to the *InputModule.py*


**Code Components**
* Analyzermodulenew.sh --> Generates time, gcov, gprof information and stores it in ./Results/appTest/run*count* file for each count in the input file.
* AnalyzerModuleOracle.sh --> Executes the Oracle gets time information. Or the time information can be provided in a file. It stores the information in ./Results/Oracle/run*count* for each count in file.
* FileEdit.py : Analyzes the time information. Choose traces who have times greater than the oracle time by a certain percentage. **BadTraces**
* CoverageStat.py: Create overalpping block traces from the previously chosen **bad traces**
* SeminalBehaviour.py - Create the seminal feature set from the aforementioned block traces. 
* Analysis.py - Generates new population of inputs. 
* Gene.py - Contains the genetic algorithm which is used by analysis.py to generate the new inputs. It uses *LMS* to derive the corelation between the seminal features and the new inputs. We could use another learning tool to replace/supplement the input generation. 
* Visualization.py - Creates a graph for input time of application under test vs input time for oracle for the current population. Creates a cummalative coverage html page for the current population where overalpping areas are highlighted in red and the lines not executed at all are highlighted in blue. 
* Evaluation.py - Moves the graph and the html stat file to folder ./Results/Runs/Runnum

The Process iterates over again generating new input for each run.

**Parts that can be Switched out**
* Features chosen for seminal SeminalBehaviour can be switched. Right now inputs from stdin and function frequency count is considered.
* The Learning that generates the new population can be changed.
* The Profiling tool can be switched. 

**Current test Code**
*Application under Test*: CustomBS.c -> an application of binary sort off the internet. 
*Oracle*: bs.o -> (Source is not required) A benchmark implementation from the site : WCET 

**Generated status file**
[link](./Results/Runs/0/combinedGcda.html)


**Current Project Architecture**

![alt-text](./Results/Runs/OverallArchitecture.png "OverallArchitecture")

**Reference**
- Exploiting Statistical Correlations for Proactive Prediction of Program Behaviors - Yunlian Jian et all
- An Input-Centric Paradigm for Program Dynamic Optimizations - Kai Tian, Yunlian Jian


