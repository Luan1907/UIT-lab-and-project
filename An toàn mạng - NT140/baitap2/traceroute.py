from scapy.all import *

inRoute = True
i = 1
while inRoute:
	a = IP(dst='192.168.1.20', ttl=i)
	response = sr1(a/ICMP(),timeout=1,verbose=0)

	if response is None:
		print(f"{i} Request timed out.")
	elif response.type == 0:
		print(f"{i} {response.src}")
		inRoute = False
	else:
		print(f"{i} {response.src}")

	i = i + 1
