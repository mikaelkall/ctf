#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter
from pwnlib.util.fiddling import randoms

level = 22
user = 'bandit%s' % level
next_user = 'bandit%s' % str(level+1)
host = 'bandit.labs.overthewire.org'
password = 'Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

_check="I am user %s" % next_user

sh = connectToLevel()
p = sh.process("echo %s | md5sum | cut -d ' ' -f1" % _check, shell=True)
checksum = p.recvline()

_sh = connectToLevel()
p = _sh.process("cat /tmp/%s" % checksum, shell=True)
log.info('Flag = %s' % p.recvline())
