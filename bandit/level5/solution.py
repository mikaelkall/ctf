#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter

level = 5
user = 'bandit%s' % level
host = 'bandit.labs.overthewire.org'
password = 'koReBOKuIDDepwhWk7jZC0RTdopnAYKh'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process(['find', './inhere','-size','1033c'])
filename=p.recvline().strip()
p = sh.process(['cat', filename])
log.info('Flag = %s' % p.recvline())
