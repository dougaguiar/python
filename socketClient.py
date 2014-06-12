#!/usr/bin/python
import socket
import sys
import numpy as np
import pickle

size = 10
deviation = 0.1

signalIx = 2*np.random.randint(2, size=size)-1+np.random.normal(0,deviation,size)
signalQx = 2*np.random.randint(2, size=size)-1+np.random.normal(0,deviation,size)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
try:
	# Send data
	# message = 'This is the message.  It will be repeated.'
	message = pickle.dumps(signalIx)
	print >>sys.stderr, 'sending "%s"' % message
	sock.sendall(message)
	
	# Look for the response
	amount_received = 0
	amount_expected = len(message)
	
	while amount_received < amount_expected:
		data = sock.recv(16)
		amount_received += len(data)
		print >>sys.stderr, 'received "%s"' % data
finally:
	print >>sys.stderr, 'closing socket'
	sock.close()
