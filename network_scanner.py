import scapy.all as scapy
import argparse as ag

def get_arguments():
	parser = ag.ArgumentParser()
	parser.add_argument('-t', '--target', help = 'ip range')	
	args = parser.parse_args()
	return args

def scan(ip):
	arp_pkt = scapy.ARP(pdst = ip)
	broadcast =  scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')
	arp_broadcast = broadcast/arp_pkt
	ans_list = scapy.srp(arp_broadcast, timeout = 1)[0]
	
	print('IP \t\t MAC')
	for element in ans_list:
		print('-'*35)
		print(element[1].psrc, end ='')
		print('\t'+element[1].hwsrc)


args = get_arguments()	
scan(args.target)
print('My ip not scanned')