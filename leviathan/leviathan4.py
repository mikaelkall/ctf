#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter
from pwnlib.util.fiddling import randoms
from time import sleep

level = 4
user = 'leviathan%s' % level
host = 'leviathan.labs.overthewire.org'
password = 'vuH0coox6m'
port = 2223

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()

p = sh.process('rax2 -b $(.trash/bin)', shell=True)
log.info('Flag = %s' % p.recvline())