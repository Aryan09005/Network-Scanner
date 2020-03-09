import scapy.all as scapy
import argparse as ag

def get_arguments():
	"""This is to get user in put"""
	parser = ag.ArgumentParser()
	parser.add_argument('-t', '--target', help = 'ip range')	
	args = parser.parse_args()
	return args

def scan(ip):
	"""This will scan ip(s)"""
	arp_pkt = scapy.ARP(pdst = ip)
	broadcast =  scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')
	arp_broadcast = broadcast/arp_pkt
	ans_list = scapy.srp(arp_broadcast, timeout = 1)[0]
	
	"""
	This part will print the result of the ans_list list. Printing the ip and the respective mac
	
	"""
	print('IP \t\t MAC')
	for element in ans_list:
		print('-'*35)
		print(element[1].psrc, end ='')
		print('\t'+element[1].hwsrc)


"""Now we call the above methods in order"""
args = get_arguments()	
scan(args.target)
print('My ip not scanned')
