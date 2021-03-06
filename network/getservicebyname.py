# -----------------------------------------------------------
# demonstrates identifying ports by its service name
#
# (C) 2016 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# based on: A Simple TCP Client and Server described in the 
# book from Brandon Rhodes and John Goerzen: 
# Foundations of Python Network Programming
# apress, 2010, ISBN 978-1-4302-3003-8
# -----------------------------------------------------------

import socket

# define list of network services
protocolList = ['www', 'ftp', 'ssh', 'pop3']

for protocol in protocolList:
	port = socket.getservbyname(protocol)

	# print port and protocol as well-formatted output
	print ('%6s: %3i' % (protocol, port))

