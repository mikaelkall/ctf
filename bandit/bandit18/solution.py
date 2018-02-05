#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter
from pwnlib.util.fiddling import randoms
from time import sleep

level = 18
user = 'bandit%s' % level
host = 'bandit.labs.overthewire.org'
password = 'kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process("cat readme",shell=True)
log.info('Flag = %s' % p.recvline())
