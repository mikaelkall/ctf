#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter

level = 3
user = 'bandit%s' % level
host = 'bandit.labs.overthewire.org'
password = 'UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process(['cat', './inhere/.hidden'])
log.info('Flag = %s' % p.recvline())
