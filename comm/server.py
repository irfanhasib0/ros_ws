#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = '192.168.1.10'#socket.gethostname() # Get local machine name
print(host)
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   data_in=c.recv(1024)
   print(data_in)
   data_out=bytes(input(),'utf8')
   c.send(data_out)
   c.close()
s.close() 
