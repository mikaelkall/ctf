#!/usr/bin/env python
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter

level = 1
user = 'bandit%s' % level
host = 'bandit.labs.overthewire.org'
password = 'boJ9jbbUNNfktd78OOpsqOltutMc3MY1'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process(['cat', './-'])
log.info('Flag = %s' % p.recvline())