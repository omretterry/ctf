#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <arpa/inet.h>

int main(){
	FILE* fp = fopen("\x0a","wb");
	fwrite("\x00\x00\x00\x00",4,1,fp);
	fclose(fp);

	int fds[2];
	int fds2[2];
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
		char inputfile[] = "/home/ubuntu/pwnable/input";
		char *argv[101]={inputfile,[1 ... 99]="A",NULL};
		argv['A']="\x00";
		argv['B']="\x20\x0a\x0d";
		argv['C']="9999";
		fflush(stdout);
		char *env[2] = {"\xde\xad\xbe\xef=\xca\xfe\xba\xbe",NULL};
		execve(inputfile,argv,env);
		exit(1);
	}

	//socket io part
	int sock;
	struct sockaddr_in saddr;
	char buf[4];
	saddr.sin_family = AF_INET;
	saddr.sin_addr.s_addr = inet_addr("127.0.0.1");
	saddr.sin_port = htons(9999);
	sock = socket(AF_INET, SOCK_STREAM,0);
	connect(sock, (struct sockaddr*)&saddr, sizeof(saddr));
	strcpy(buf,"\xde\xad\xbe\xef");
	send(sock,buf,len(buf),0);
	close(sock);

	return 0;
}
