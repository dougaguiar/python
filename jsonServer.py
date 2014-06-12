#!/usr/bin/python

from jsonsocket import Client, Server

host = 'localhost'
port = 10000

server = Server(host, port)
while True:
	print >> 'Server listening...'
	server.accept()
	data = server.recv()
	print data
	if data:
		break
server.send({'data': data}).close()
