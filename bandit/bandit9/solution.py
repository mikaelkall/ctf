#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter

level = 9
user = 'bandit%s' % level
host = 'bandit.labs.overthewire.org'
password = 'UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process("strings data.txt |grep ======== |awk '{print length, $0}' |sort -nr |head -1 |cut -d ' ' -f3", shell=True)
log.info('Flag = %s' % p.recvline())
