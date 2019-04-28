#!/usr/bin/env python2
import re

def local():

    with open("hex_editor.jpg","rb") as f:
        binary = f.read().split("colr",1)[0]
        x = re.search(".*(picoCTF{.*})", binary)
        print(x.group(1))

if __name__ == '__main__':
	local()