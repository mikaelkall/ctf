#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter

level = 1
user = 'leviathan%s' % level
host = 'leviathan.labs.overthewire.org'
password = 'rioGegei8m'
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

exe = sh.run('./check')
exe.recvuntil('password:')
# Check the strcmp function with ltrace, objdump or gdb
# To find password sex
exe.sendline('sex')
exe.recvuntil('$')
flag = getPass(exe)
