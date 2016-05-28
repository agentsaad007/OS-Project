import socket
import sys
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
 
s.listen(10)
print 'Socket now listening'
 
def clientthread(conn):
	conn.send("Welcome to the server!\nTo Quit any time, enter 'quit()' without quotes.")
	j=0
	k=0
	while 1:
		for x in range(len(arr)):
			if arr[x]['conn']==conn:
				j=x
				break
		k=-1
		for x in range(len(arr)):
			if arr[x]['name']==arr[j]['link']:
				k=x
				break
		if k>-1:
        		data = conn.recv(1024)
			if data=='quit()':
				BroadcastAbsence(arr[j])
				del arr[j]
				break
			else:
				arr[k]['conn'].send(arr[j]['name']+':'+data)
	conn.close()
def ListAllUser(conn):
	k=1
	conn.send("\n-----Following Users are connected with server-----\n")
	loop = len(arr)
	while loop:
		loop -= 1
		if arr[loop]['conn'] != conn:
			conn.send(str(k)+'-'+arr[loop]['name']+"\n")
	conn.send("------------------------------------------------------\n")
	return
def BroadcastAbsence(temp):
	loop = len(arr)
	while loop:
		loop -= 1
		arr[loop]['conn'].send("--------------------------------------")
		arr[loop]['conn'].send("\n" + temp['name'] + " is Now Offline\n")
		arr[loop]['conn'].send("--------------------------------------")
	return
	
def BroadcastPresence(temp):
	loop = len(arr)
	while loop:
		loop -= 1
		arr[loop]['conn'].send("--------------------------------------")
		arr[loop]['conn'].send("\n" + temp['name'] + " is Now Online\n")
		arr[loop]['conn'].send("--------------------------------------")
	return
arr =[]
i = 0
while 1:
    conn, addr = s.accept()
    temp = {}
    temp['conn'] = conn
    temp['adress'] = addr
    temp['name'] = conn.recv(200)
    temp['link'] = conn.recv(200)
    BroadcastPresence(temp)
    arr += [temp]
    ListAllUser(conn)
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    start_new_thread(clientthread ,(conn,))
    i += 1
s.close()

