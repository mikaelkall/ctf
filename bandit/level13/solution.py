#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter
from pwnlib.util.fiddling import randoms
from time import sleep

level = 13
user = 'bandit%s' % level
host = 'bandit.labs.overthewire.org'
password = '8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process("ssh -i ./sshkey.private -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no bandit14@localhost cat /etc/bandit_pass/bandit14", shell=True)
log.info('Flag = %s' % p.recvlines(4)[3])
