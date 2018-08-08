#include <unistd.h>
#include <string.h>

int main(){
	int fds[2];
	pid_t pid = fork();

	if(pid == 0){
		char buf[] = "asdf";
		write(fds[1],buf,strlen(buf));
		//close(fds[1]);
		exit(0);
	}else{
		wait(NULL);
		char buf[50];
		read(fds[0],buf,sizeof(buf));
		printf(buf);
	}
}
