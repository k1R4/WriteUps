#define _GNU_SOURCE
#include <stdio.h>
#include <unistd.h>

#include <stdlib.h>
#include <string.h>

        print("Generating....")
        try:
                os.chmod(tmpdirname, 0755)
                shufproc = subprocess.run([mangler, "--seed", str(randseed), "-sbCMSr", "--shimalign", "1", sourcefile, tmpdirname + "/source_mangled"], check=True, timeout=2, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
                print_exc()
                print("Shuf failed, contact admins")
                pass
        try:
                linkproc = subprocess.run(["gcc", "-no-pie", tmpdirname + "/source_mangled", "-o", tmpdirname + "/source_fin"], check=True, timeout=2, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
                print_exc()
                print("link failed, contact admins")
                pass
        print("Finished generating with seed {}".format(randseed))

//radare2 4.1.1 (has to be this version!)
//we are using a modded version of https://github.com/siegetechnologies/virtue/tree/master/linux/userspace/elf-mangler located at https://drive.google.com/file/d/16C28YAW_o8Ai7eLEZqvkzICLyMSLcn-M/
//gcc version 9.3.0 (Ubuntu 9.3.0-17ubuntu1~20.04) (i dont think it matters)

//password was HuN7erTw0 if you didnt figure that out already
//get me a shell!
int getpw(void){
        struct {char pw[32];int res;} l;
        l.res = 0;
        fgets(l.pw, 322, stdin);
        *strchrnul(l.pw, '\n') = 0;
        if(!strcmp(l.pw, getenv("SOURCE1_PW"))) l.res = 1;
        return l.res;
}
char *lesscmd[] = {"less", "source.c", 0};
int main(void){
        setenv("LESSSECURE", "1", 1);
        printf("Enter the password to get access to https://www.imdb.com/title/tt4248106/\n");
        if(!getpw()){
                printf("Pasword auth failed\nexiting\n");
                return 1;
        }

        execvp(lesscmd[0], lesscmd);
        return 0;
}