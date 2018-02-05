#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter
from pwnlib.util.fiddling import randoms

level = 25
user = 'bandit%s' % level
next_user = 'bandit%s' % str(level+1)
host = 'bandit.labs.overthewire.org'
password = 'uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process("ssh -i bandit26.sshkey bandit26@localhost", shell=True)
p.interactive()
