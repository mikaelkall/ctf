#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter

level = 11
user = 'bandit%s' % level
host = 'bandit.labs.overthewire.org'
password = 'IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process("cat data.txt | tr '[A-Za-z]' '[N-ZA-Mn-za-m]' | cut -d ' ' -f4", shell=True)
log.info('Flag = %s' % p.recvline())
