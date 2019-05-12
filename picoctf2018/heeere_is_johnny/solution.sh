#!/bin/bash
SCRIPT_DIR=$(dirname $0)
cd ${SCRIPT_DIR}

# Create hash folder
unshadow ./passwd ./shadow > hashes.hash

[ ! -e '/usr/share/wordlist/SecLists/Passwords/Leaked-Databases/rockyou.txt' ] && echo "[-] Missing dictionary rockyou.txt." && exit

# Crack shadow file
hashcat -m 1800  -a 0 -o results.txt ./hashes.hash /usr/share/wordlist/SecLists/Passwords/Leaked-Databases/rockyou.txt

[ ! -e './results.txt' ] && echo "[-] Cracking failed." && exit

PASSWORD=$(cat ./results.txt | cut -d':' -f2 | xargs)

echo -e "\n\n"
echo -e "root\n${PASSWORD}\n" | nc 2018shell.picoctf.com 38860
echo -e "\n\n"