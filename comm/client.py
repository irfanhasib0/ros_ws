#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = '192.168.1.10'#socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.


while(1):
	s = socket.socket()
	data_out= bytes(input(),'utf8')
	s.connect((host, port))
	s.send(data_out)
	print(s.recv(1024))
	s.close()                     # Close the socket when done
