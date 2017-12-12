#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter
from pwnlib.util.fiddling import randoms
from time import sleep

level = 14
user = 'bandit%s' % level
host = 'bandit.labs.overthewire.org'
password = '4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process("echo %s | nc localhost 30000" % password, shell=True)
log.info('Flag = %s' % p.recvlines(2)[1])
