#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level8.py
  Solution for natas level8
"""
__author__ = 'kall.micke@gmail.com'

import requests
import sys
import os
import re
import base64
import binascii

level = 8 
user = 'natas%s' % level
host = 'http://natas%s.natas.labs.overthewire.org' % level
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'
encodedSecret = '3d3d516343746d4d6d6c315669563362'

def get_flag():

    _secret = base64.b64decode(binascii.unhexlify(encodedSecret)[::-1])
    session = requests.Session()
    session.auth = (user, password)
    postData = {"secret": _secret, "submit":"Skicka+fr%C3%A5ga"}
    r = session.post(host, data=postData)
    return str([c for c in r.text.split('\n') if 'The password for natas9' in c][0].split('is')[1].split()[0])

if __name__ == '__main__':
    print("Flag: %s" % get_flag())
