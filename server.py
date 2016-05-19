import socket
import sys
conn=[0,0]
from thread import * 
HOST = ''
PORT = 5188
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created' 

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()     
print 'Socket bind complete'
s.listen(2)
print 'Socket now listening'
 
def clientthread1(c1):
	c1.send('***Welcome to the server***\n')
    	while True:
		data = c1.recv(1024)
		if c1==conn[0]:		        
			conn[1].send(data)
		elif c1==conn[1]:        
			conn[0].send(data)
i=0	
while 1:
    	conn[i], add = s.accept()
	print 'Connected with ' + str(add[0]) + ':' + str(add[1])
	start_new_thread(clientthread1 ,(conn[i],))
	i=i+1
s.close()
