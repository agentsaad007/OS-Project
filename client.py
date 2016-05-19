

import socket               
from thread import *

s = socket.socket()         
host = socket.gethostname()
port = 5188                
s.connect((host, port))
x=s.recv(1024)
print x

def func(s):
	while 1:
		x=s.recv(1024)
		print x

start_new_thread(func,(s,))
while 1:
	x=raw_input()	
	if x=='Q' or  x=='q':
		break
	else:
		s.send("Other Person : "+x)
s.close()             
