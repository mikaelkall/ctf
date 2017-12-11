#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter

level = 8
user = 'bandit%s' % level
host = 'bandit.labs.overthewire.org'
password = 'cvX2JJa4CFALtqS87jk27qwqGhBM9plV'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process('sort data.txt | uniq -u', shell=True)
log.info('Flag = %s' % p.recvline())
