#!/usr/bin/env python
from pwn import *
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import TerminalFormatter
import base64
import string
import re

# Take the first available device
context.device = '127.0.0.1:5555'

# Note ADB needs to be in root mode. [adb root]
data = adb.read('/data/data/com.mobshep.insecuredata1/databases/Users')
plain = filter(lambda x: x in set(string.printable), data)
encoded = "%s==" % str(re.search('Root(.*)==-', plain).group(1))

print "Flag: %s" % base64.b64decode(encoded)
