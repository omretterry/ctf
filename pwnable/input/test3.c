#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(){
	//setenv("\xde\xad\xbe\xef","\xca\xfe\xba\xbe",1);
	char *env[2] = {"\xde\xad\xbe\xef=\xca\xfe\xba\xbe",NULL};
	execve("/home/ubuntu/pwnable/input3",NULL,env);	
	return 0;
}
