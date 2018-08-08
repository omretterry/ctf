#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(){
	FILE *fp = fopen("\x0a","wb");
	if(!fp){
		perror("can not read file");
		exit(1);
	}
	fwrite("\x00\x00\x00\x00",4,1,fp);
	fclose(fp);
	execve("/home/ubuntu/pwnable/input4",NULL,NULL);	
	return 0;
}
