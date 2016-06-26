
import socket
from thread import *

s = socket.socket()         
host = socket.gethostname()
port = 6188
s.connect((host, port))
x= raw_input("Enter Your Name : ")
s.send(x)


def func(s):
    while 1:
        x = s.recv(1024)
        print x


start_new_thread(func, (s,))
while 1:
    x = raw_input()
    if x == 'quit()':
        s.send(x)
        break
    else:
        s.send(x)
s.close()
