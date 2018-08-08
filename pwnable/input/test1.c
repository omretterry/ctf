#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(){
	char *argv[101] = {"/home/ubuntu/pwnable/input1",[1 ... 99]="A", NULL};
	argv['A']="\x00";
	argv['B']="\x20\x0a\x0d";
	fflush(stdout);
	//printf("-i---before----");
	execve("/home/ubuntu/pwnable/input1",argv,NULL);
	//printf("----after----");	
	
	return 0;
}
