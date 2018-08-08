#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <arpa/inet.h>

int main(){
	char *argv[101]={"/home/ubuntu/pwnable/input5",[1 ... 99]="A",NULL};
	argv['C']="9999";
	execve("/home/ubuntu/pwnable/input5",argv,NULL);
	sleep(2);
	int sock;
	struct sockaddr_in saddr;
	char buf[4];
	saddr.sin_family = AF_INET;
	saddr.sin_addr.s_addr = inet_addr("127.0.0.1");
	saddr.sin_port = htons(9999);
	sock = socket(AF_INET, SOCK_STREAM, 0);
	connect(sock, (struct sockaddr*)&saddr, sizeof(saddr));
	strcpy(buf,"\xde\xad\xbe\xef");
	send(sock,buf,strlen(buf),0);
	close(sock);
	return 0;
}
