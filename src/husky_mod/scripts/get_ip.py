import netifaces as ni
def ip_addr():
	ni.ifaddresses('wlp1s0')
	ip = ni.ifaddresses('wlp1s0')[ni.AF_INET][0]['addr']
	print(ip)  # should print "192.168.100.37"
ip_addr()
