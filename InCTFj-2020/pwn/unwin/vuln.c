#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFFSIZE 80
#define NAMESIZE 100


int vuln(){

	setvbuf(stdout, NULL, _IONBF, 0);
	gid_t gid = getegid();
	setresgid(gid, gid, gid);

	char name[NAMESIZE];
	
	puts("============ Super Secure Machine =============");
	printf("Enter Your Name : " );
	fgets(name,10,stdin);
	printf("Welcome Agent " );
	printf(name);

	char buf[BUFFSIZE];
	printf(">>", name);
	gets(buf);
	return 0;

}

int main(int argc, char **argv){
	vuln();
	return 0;
}
