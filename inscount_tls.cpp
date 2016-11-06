/*BEGIN_LEGAL 
Intel Open Source License 

Copyright (c) 2002-2016 Intel Corporation. All rights reserved.
 
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.  Redistributions
in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or
other materials provided with the distribution.  Neither the name of
the Intel Corporation nor the names of its contributors may be used to
endorse or promote products derived from this software without
specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE INTEL OR
ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
END_LEGAL */
#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>
#include "pin.H"
#include <time.h>
#include<algorithm>


//Global variables
std::vector<ADDRINT>* consecutive_indirect_bbls = new std::vector<ADDRINT>();
std::vector<ADDRINT>* alreadyvisited = new std::vector<ADDRINT>();
std::ostream& Output = std::cout;
time_t timet;

    
// Pin calls this function every time a new basic block is encountered
// It inserts a call to docount



VOID analysis_indirect(ADDRINT  address)
{
  consecutive_indirect_bbls -> push_back(address);
}

/*
VOID analysis_print_vector() {
    	
    if (consecutive_indirect_bbls->size() > 2) {	
        for (unsigned int i = 0;i < consecutive_indirect_bbls->size();++i) {
            Output << "0x" << std::hex << consecutive_indirect_bbls->at(i) << " -> ";
        }
	
        Output << " END" << std::endl;	
        consecutive_indirect_bbls->clear();
    } else if (!consecutive_indirect_bbls->empty()) {
        consecutive_indirect_bbls->clear();	
    }
}*/

VOID Fini(INT32 code, VOID *v)
{
	unsigned int i =0;
	for(i = 0; i < consecutive_indirect_bbls->size(); ++i)
	{
		 Output << "0x" << std::hex << consecutive_indirect_bbls->at(i) << " -> ";	
	}
	Output << " END" << std::endl;	
} 


VOID BlkTrace(TRACE trace, VOID *v)
{
    // Visit every basic block  in the trace
     	
    for (BBL bbl = TRACE_BblHead(trace); BBL_Valid(bbl); bbl = BBL_Next(bbl))
    {
	
	ADDRINT present_addr=BBL_Address(bbl);
	if(std::find(alreadyvisited->begin(), alreadyvisited->end(), present_addr) != alreadyvisited-> end())
	{
			//Present addr is present
			alreadyvisited -> push_back(present_addr);
	}else
	{		
		//Present addr is not present
		BBL_InsertCall(bbl, IPOINT_BEFORE, (AFUNPTR)analysis_indirect,IARG_ADDRINT,BBL_Address(bbl), IARG_END);
		alreadyvisited -> push_back(present_addr);
	}	
		
	
	
    }
    		
}

KNOB<string> KnobOutputFile(KNOB_MODE_WRITEONCE, "pintool",
    "o", "inscount.out", "specify output file name");


/* ===================================================================== */
/* Print Help Message                                                    */
/* ===================================================================== */

INT32 Usage()
{
    cerr << "This tool prints a trace of the blocks executed" << endl;
    cerr << endl << KNOB_BASE::StringKnobSummary() << endl;
    return -1;
}

/* ===================================================================== */
/* Main                                                                  */
/* ===================================================================== */

int main(int argc, char * argv[])
{
    // Initialize pin
    if (PIN_Init(argc, argv)) return Usage();

   

    // Register Instruction to be called to instrument instructions
    TRACE_AddInstrumentFunction(BlkTrace, 0);
    PIN_AddFiniFunction(Fini, 0);	
     
    // Start the program, never returns
    PIN_StartProgram();
    
    return 0;
}
