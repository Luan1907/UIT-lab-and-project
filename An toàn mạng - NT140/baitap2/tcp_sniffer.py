#!/usr/bin/python

from scapy.all import *

def print_pkt(pkt):
	if pkt[TCP] is not None:
		print("TCP Packet=====")
		print(f"\tSource: {pkt[IP].src}")
		print(f"\tDestination: {pkt[IP].dst}")
		print(f"\tTCP Source port: {pkt[TCP].sport}")
		print(f"\tTCP Destination port: {pkt[TCP].dport}")


interfaces = ['br-e8d2b02fb7f9','eth0','lo']
pkt = sniff(iface=interfaces, filter='tcp port 23 and src host 10.9.0.6', prn=print_pkt)
