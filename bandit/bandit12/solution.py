#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter
from pwnlib.util.fiddling import randoms
from time import sleep

level = 12
user = 'bandit%s' % level
host = 'bandit.labs.overthewire.org'
password = '5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu'
port = 2220

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

context(arch='i386', os='linux')

# Base folder for unpack
UNPACK_FOLDER='/tmp/%s' % randoms(10)

# Unpack binary
sh = connectToLevel()
sh = sh.process('/bin/sh', env={'PS1':''})
sh.sendline('mkdir -p %s' % UNPACK_FOLDER)
sleep(0.5)
sh.sendline('xxd -r ./data.txt > %s/data.gz' % UNPACK_FOLDER)
sleep(0.5)
sh.sendline('cd %s' % UNPACK_FOLDER)
sleep(0.5)
sh.sendline('gunzip data.gz')
sleep(0.5)
sh.sendline('bzip2 -d data')
sleep(0.5)
sh.sendline('mv ./data.out ./data4.gz')
sleep(2)
sh.sendline('gzip -d ./data4.gz')
sleep(0.5)
sh.sendline('tar -xvf ./data4')
sleep(0.5)
sh.sendline('tar -xvf ./data5.bin')
sleep(0.5)
sh.sendline('bzip2 -d data6.bin')
sleep(0.5)
sh.sendline('tar -xvf data6.bin.out')
sleep(0.5)
sh.sendline('mv ./data8.bin ./data8.gz')
sleep(0.5)
sh.sendline('gunzip ./data8.gz')

# Read flag
_sh = connectToLevel()
_sh = _sh.process('/bin/sh', env={'PS1':''})
_sh.sendline("cat %s/data8 |cut -d ' ' -f4" % UNPACK_FOLDER)
log.info('Flag = %s' % _sh.recvline())
