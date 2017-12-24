#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level0.py
  Solution for natas level0
"""
__author__ = 'kall.micke@gmail.com'

import requests
import sys
import os
import re

level = 0
user = 'natas%s' % level
host = 'http://natas0.natas.labs.overthewire.org'
password = 'natas0'

def authenticate():

    r = requests.get(host, auth=(user, password))
    return r

def get_flag():
    content = authenticate()
    return str([c for c in content.text.split('\n') if 'The password for natas1' in c][0].split('is')[1].split()[0])

if __name__ == '__main__':
    print("Flag: %s" % get_flag())
