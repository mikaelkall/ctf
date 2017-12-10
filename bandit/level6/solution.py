#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter

level = 6
user = 'bandit%s' % level
host = 'bandit.labs.overthewire.org'
password = 'DXjZPULLxYr17uwoI01bNLQbtFemEgo7'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process('find / -group bandit6 -user bandit7 2>/dev/null', shell=True)
filename=p.recvall().strip()
p = sh.process(['cat', filename])

log.info('Flag = %s' % p.recvline())
