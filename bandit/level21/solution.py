#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter
from pwnlib.util.fiddling import randoms
from time import sleep

level = 21
user = 'bandit%s' % level
host = 'bandit.labs.overthewire.org'
password = 'gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process("cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv",shell=True)
log.info('Flag = %s' % p.recvline())
