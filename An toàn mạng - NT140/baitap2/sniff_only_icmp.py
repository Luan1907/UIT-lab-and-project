#!/usr/bin/python

from scapy.all import *

def print_pkt(pkt): 

	if pkt[ICMP] is not None:
		if pkt[ICMP].type == 0 or pkt[ICMP].type == 8:
			print("ICMP Packet=====")
			print(f"\tSource: {pkt[IP].src}")
			print(f"\tDestination: {pkt[IP].dst}")

			if pkt[ICMP].type == 0:
				print(f"\tICMP type: echo-reply")
			if pkt[ICMP].type == 8:
				print(f"\tICMP type: echo-request")



interfaces = ['br-e8d2b02fb7f9','eth0','lo']
pkt = sniff(iface=interfaces, filter='icmp', prn=print_pkt)
