#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level2.py
  Solution for natas level2
"""
__author__ = 'kall.micke@gmail.com'

import requests
import sys
import os
import re

level = 2
user = 'natas%s' % level
host = 'http://natas%s.natas.labs.overthewire.org' % level
password = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'

def authenticate():

    r = requests.get(host + '/files/users.txt', auth=(user, password))
    return r

def get_flag():
    content = authenticate()
    return str([c for c in content.text.split('\n') if 'natas3' in c][0].split(':')[1])

if __name__ == '__main__':
    print("Flag: %s" % get_flag())
