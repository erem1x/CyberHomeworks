#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

//GLOBAL STATS

int lowest_b1=0;
int lowest_b2=0;

int lowest_w1=0;
int lowest_w2=0;

int avg1=0;
int avg2=0;


void generate(char* buf){
	char line[130];
	FILE *fp;
	fp=popen(buf, "r");
	
	//Command + data analisys for each run
	while(fgets(line, sizeof(line), fp)){
		printf("%s", line);
    }
    pclose(fp);
}



int main(int argc, char *argv[] ){
	//Check validity of input arguments
	if(argc!=2){
		fprintf(stderr, "Error\nPassword required!\n");
		exit(-1);
	}
	
	//Defining command
	char buf[32];
	sprintf(buf, "./kdf.sh %s", argv[1]);
	generate(buf);
	
	
    
     
	
	return(0);
}
