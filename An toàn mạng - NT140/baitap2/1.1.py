#!/usr/bin/env python3
from scapy.all import *
def print_pkt(pkt):
	pkt.show()
pkt = sniff(iface= "br-e8d2b02fb7f9", filter="icmp", prn=print_pkt)
