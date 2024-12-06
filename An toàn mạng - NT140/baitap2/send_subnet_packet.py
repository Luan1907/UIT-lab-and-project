from scapy.all import *
ip=IP()
ip.dst='128.230.0.0/16'
send(ip,iface="eth0",loop = 0,inter = 5)
