from scapy.all import *
a = IP()
a.src = '1.2.3.4'
a.dst = '192.168.179.131'
send(a/ICMP())
ls(a)
