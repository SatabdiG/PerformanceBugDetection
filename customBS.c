//Binary Sort Code written for evaluation
#include<stdio.h>
#include<stdlib.h>
#include<time.h>


struct DATA {
  int  key;
  int  value;
}  ;

struct DATA data[15] = { {1, 100},
	     {5,200},
	     {6, 300},
	     {7, 700},
	     {8, 900},
	     {9, 250},
	     {10, 400},
	     {11, 600},
	     {12, 800},
	     {13, 1500},
	     {14, 1200},
	     {15, 110},
	     {16, 140},
	     {17, 133},
	     {18, 10} };

int binarySort(int);

int main(int argc, char *argv[])
{
	int input, retval;
    
	if(argc!=2)
	{
		printf("Please enter ProgramName NumberToSearch !!\n");
		exit(0);
	}
	else
	{
		//Enter Binary Sort Code Here
		input=atoi(argv[1]);
		retval=binarySort(input);
		if(retval == -1)
			printf("\nSorry Number not found!!\n");
		else
		{
			printf("\nNumber found %d\n",retval);
		}	
		
	}	

	return 0;
}

int binarySort(int val)
{
	int retval, midpoint;
	int low=0;	
	int  high=14;	
	int flag=0;
	int besafe=0;
	
	
	while(low<=high)
	{	
		midpoint=(low+high)/2;
		besafe+=1;
		printf("%d  %d %d\n",high,low,midpoint);
		
		printf("%d\n",data[midpoint].key);
		if(data[midpoint].key == val)
		{
			//Found
			printf("Found!!\n");
			flag=1;
			return data[midpoint].value;
			
		}else
		{
		   //create new midpoint
	          if(data[midpoint].key <= val)
		 {
		   low=midpoint;
		   high=high;		
                 }
		  else
		{
                  high=midpoint;
		  low=low;	
		}
		 
		}
		if(besafe>=10000)
		{
			return -1;
		} 
		
	}
	if(flag == 0)
	{
		high=-1;
		return high;
		
	}
		

}
