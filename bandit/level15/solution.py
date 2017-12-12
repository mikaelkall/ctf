#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter
from pwnlib.util.fiddling import randoms
from time import sleep

level = 15
user = 'bandit%s' % level
host = 'bandit.labs.overthewire.org'
password = 'BfMYroe26WYalil77FoDi9qh59eK5xNr'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process("echo %s | openssl s_client -ign_eof -quiet -connect localhost:30001" % password, shell=True)
log.info('Flag = %s' % p.recvlines(7)[6])
