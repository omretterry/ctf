#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <arpa/inet.h>

int main(){
	/* stage 5 */
    sleep(2); // wait the server start
    int sockfd;
    char buf[10] = {0}; // buf to be sent
    int len;            // len of avail buf
    struct sockaddr_in servaddr;
    servaddr.sin_family = AF_INET;  
    servaddr.sin_port = htons(9999);  // port in argv['C'] 
    servaddr.sin_addr.s_addr = inet_addr("127.0.0.1"); //local
    if( (sockfd = socket(PF_INET, SOCK_STREAM, 0)) < 0 )  
    {  
        perror("socket error.");  
        exit(1);  
    }  
    if ( connect(sockfd, (struct sockaddr*) &servaddr, sizeof(servaddr)) < 0 )
    {
        perror("connect error.");
        exit(1);
        }
    printf("socket connect.\n");
    strcpy(buf, "\xde\xad\xbe\xef");
    len = strlen(buf);
    send(sockfd, buf, len, 0);
    close(sockfd);
}
