#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


#define BUFFERSIZE 64

void init(){
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

int win(int arg){
	char shell[50] = "/bin/sh";
	if(arg == 0xdeadbeef){
		system(shell);
	}
}

int get_name(){
	char buf[BUFFERSIZE];
	fgets(buf,0x60,stdin);
	printf("Hello %s",buf);
}

int main(){
	init();
	puts("Super Secure Login");
	puts("----------------------\n");
	printf("Enter your name: ");
	get_name();
}
