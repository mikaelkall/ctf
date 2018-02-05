#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter

level = 2
user = 'bandit%s' % level
host = 'bandit.labs.overthewire.org'
password = 'CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process(['cat', './spaces in this filename'])
log.info('Flag = %s' % p.recvline())
