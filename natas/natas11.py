#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level11.py
  Solution for natas level11
"""
__author__ = 'kall.micke@gmail.com'

import requests
import sys
import os
import re
import base64

from urllib import unquote

level = 11
user = 'natas%s' % level
host = 'http://natas%s.natas.labs.overthewire.org' % level
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'
cookie='ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw='

def get_key():

    y = '{"showpassword":"no","bgcolor":"#ffffff"}'
    x = base64.b64decode(unquote(cookie))

    key = ''
    for c1, c2 in zip(x, y):
        key += chr(ord(c1) ^ ord(c2))

    return key[:4]

def xor_encrypt(data):
    key = get_key()
    out = ''

    for i, d in enumerate(data):
        out += chr(ord(d) ^ ord(key[i % len(key)]))

    return out

def get_flag():

    _payload = '{"showpassword":"yes","bgcolor":"#ffffff"}' 
    _cookie =  dict(data=base64.b64encode(xor_encrypt(_payload))) 

    r = requests.get(host, auth=(user, password), cookies=_cookie)
    return str([c for c in r.text.split('\n') if 'The password for natas12' in c][0].split('is')[1].split()[0]).replace('<br>','')

if __name__ == '__main__':
    print("Flag: %s" % get_flag())
