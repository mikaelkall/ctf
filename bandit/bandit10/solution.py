#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter

level = 10
user = 'bandit%s' % level
host = 'bandit.labs.overthewire.org'
password = 'truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process("cat data.txt |base64 -d | cut -d ' ' -f4", shell=True)
log.info('Flag = %s' % p.recvline())
