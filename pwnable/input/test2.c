#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(){
	int fds[2];//stdin pipe
	int fds2[2];//stderr pipe
	pipe(fds);
	pipe(fds2);
	pid_t pid = fork();
	if(pid == 0){
		close(fds[0]);
		close(fds2[0]);
		write(fds[1],"\x00\x0a\x00\xff",5);
		write(fds2[1],"\x00\x0a\x02\xff",5);
	} else {
		close(fds[1]);
		close(fds2[1]);
		dup2(fds[0],0);
		close(fds[0]);
		dup2(fds2[0],2);
		close(fds2[0]);
		execve("/home/ubuntu/pwnable/input2",NULL,NULL);
	}

//	execve("/home/ubuntu/pwnable/input2",NULL,NULL);
	
	return 0;
}
