#!/usr/bin/env python
import r2pipe
r = r2pipe.open('./main')
code = r.cmd('pcp 0x19 @obj.sekrutBuffer')
exec(code)

greet = "You have now entered the Duck Web"

flag = ""
for i, byte in enumerate(buf):
    flag += chr(byte ^ ord(greet[i]))

print(flag)
