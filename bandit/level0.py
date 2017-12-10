#!/usr/bin/env python
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter

level = 0
user = 'bandit%s' % level
host = 'bandit.labs.overthewire.org'
password = 'bandit0'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process(['cat', 'readme'])
log.info('Flag = %s' % p.recvline())