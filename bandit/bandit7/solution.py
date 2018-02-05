#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter

level = 7
user = 'bandit%s' % level
host = 'bandit.labs.overthewire.org'
password = 'HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process('cat ./data.txt | grep millionth | cut -f2', shell=True)
log.info('Flag = %s' % p.recvline())
