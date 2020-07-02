#!/usr/bin/env python

import socket

class PortScanner:

	open_ports=[]
	closed_ports=[]

	def scan_ports(self, target_host, start_port, end_port):
		for pn in range(start_port,end_port+1):   #make sure the last port is included in the scan
			opened_socket = None

			try:
				opened_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				opened_socket.settimeout(3)    #give up is the connection attempt hangs
				con = opened_socket.connect((target_host,pn))
				print('Port',pn,' on host ',target_host, ' is OPEN.')	
				self.open_ports.append(pn)
			except:
				print('Port',pn,' on host ',target_host, ' is closed.')	
				self.closed_ports.append(pn)
			try:
				opened_socket.shutdown(socket.SHUT_WR)
				opened_socket.close()
			except:
				pass	
 
	def get_open_ports(self):
		return self.open_ports

	def get_closed_ports(self):
		return self.closed_ports


if __name__ == '__main__':
	our_target="www.google.com"
	begin_port=79
	last_port=81
	our_target=input('Target host: ')
	begin_port=input('Start port: ')
	last_port=input('End port: ')
	pc=PortScanner()
	pc.scan_ports(our_target, int(begin_port), int(last_port))
	print('\nSummary:\n')
	print('OPEN ports: ',pc.get_open_ports())
	print('CLOSED ports: ', pc.get_closed_ports())
	


	
