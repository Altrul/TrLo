import socket
import fcntl
import struct
import os
import time
import threading

for interface in os.listdir('/sys/class/net/'):
	if 'wireless' in os.listdir('/sys/class/net/' + interface + '/'):
		break

ifname = interface.encode()

def get_ip():
	s = socket.socket()
	a = struct.pack('256s', ifname[:15])
	b = fcntl.ioctl(s.fileno(), 0x8915, a)[20:24]
	ip = socket.inet_ntoa(b)
	return ip

def get_mask():
	s = socket.socket()
	a = struct.pack('256s', ifname[:15])
	b = fcntl.ioctl(s.fileno(), 0x891b, a)[20:24]
	ip = socket.inet_ntoa(b)
	return ip

def get_broadcast_ip():
	ip = list(map(int, this_ip.split('.')))
	mask = list(map(int, get_mask().split('.')))
	mask = list(map(lambda x:x^0xff, mask))
	brd_ip = '.'.join(list(map(lambda a:str(a[0] | a[1]), zip(ip, mask))))
	return brd_ip

def send_greeting():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	while not exit:
		sock.sendto(b'TRLO', (brd_ip, 4358))
		time.sleep(5)
	sock.close()

clients = []

def listen():
	global clients

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(('0.0.0.0', 4358))
	while True:
		data = sock.recvfrom(1024)
		if data[0] == b'TRLO':
			if data[1][0] != this_ip:
				if data[1][0] not in clients:
					clients.append(data[1][0])
					print(clients[-1])
		time.sleep(5)

exit = False

this_ip = get_ip()
brd_ip = get_broadcast_ip()
shout_thread = threading.Thread(target=send_greeting)
shout_thread.start()
listen_thread = threading.Thread(target=listen)
listen_thread.start()

while True:
	command = input('\nTrLo > ')
	if command == 'exit':
		exit = True
		break
	elif command == 'list':
		print('\n'.join(clients))