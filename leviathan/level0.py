#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter

level = 0
user = 'leviathan%s' % level
host = 'leviathan.labs.overthewire.org'
password = 'leviathan0'
port = 2223

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()

p = sh.process('cat .backup/bookmarks.html |egrep -o "the password for leviathan1 is \w+" | awk \'{ print $NF }\'', shell=True)
log.info('Flag = %s' % p.recvline())
