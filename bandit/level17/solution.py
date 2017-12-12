#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter
from pwnlib.util.fiddling import randoms
from time import sleep

level = 17
user = 'bandit%s' % level
host = 'bandit.labs.overthewire.org'
password = ''
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password, keyfile='./key.pem')

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process("bash -c 'comm -32 <(sort -i passwords.new) <(sort -i passwords.old)'",shell=True)
log.info('Flag = %s' % p.recvline())
