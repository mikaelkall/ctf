#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import sys
from scapy.all import *
from scapy2dict import to_dict
import re

def parse_packet(packet_file):

    packets = rdpcap(packet_file)
    # Let's iterate through every packet
    for packet in packets:
        if packet.haslayer(TCP):
            d = to_dict(packet, strict=True)
            try:
            	row = d['Raw']['load'].decode('utf-8')
            	x = re.search(".*(picoCTF{.*})", row)
            	print(x.group(1))
            except:
            	pass

if __name__ == '__main__':
	parse_packet('./data.pcap')
    