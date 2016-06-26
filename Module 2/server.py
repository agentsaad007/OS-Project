import socket
import sys
from thread import *

HOST = ''
PORT = 6188

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
    conn.send("Welcome to the server!\nTo Quit any time, enter 'quit()' without quotes."
              "\nEnter the name of person followed by a ':' and then your messsage to send i.e. X:Message")
    while 1:
        try:
            data = conn.recv(1024)
            for x in range(len(arr)):
                if arr[x]['conn'] == conn:
                    j = x
                    break
            if data == 'quit()':
                BroadcastAbsence(arr[j])
                print 'Disconnected with ' + arr[j]['adress'][0] + ':' + str(arr[j]['adress'][0])
                del arr[j]
                break
            else:
                k = -1
                try:
                    to, reply = data.split(':', 1)
                    for x in range(len(arr)):
                        if to == arr[x]['name']:
                            k = x
                            break
                    if k > -1:
                        arr[k]['conn'].send("Person " + arr[j]['name'] + ':' + reply)
                    else:
                        arr[j]['conn'].send("The user isn't currently available OR"
                                            " there's a mistake in name. Try again!!\n")
                except ValueError:
                    conn.send("\nWrong Format Message. Try again!\n")
                    continue
        except socket.error as error:
            j = -1
            for x in range(len(arr)):
                if arr[x]['conn'] == conn:
                    j = x
                    var = arr[j]
                    break
            if j >= -1:
                del arr[j]
                BroadcastAbsence(var)
                print 'Disconnected with ' + var['adress'][0] + ':' + str(var['adress'][0])
                break
            else:
                break
    conn.close()


def ListAllUser(conn):
    k = 1
    conn.send("\n-------Following Users are connected with server------\n")
    loop = len(arr)
    while loop:
        loop -= 1
        conn.send(str(k) + '-' + arr[loop]['name'] + "\n")
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


arr = []
i = 0
while 1:
    conn, addr = s.accept()
    temp = {}
    temp['conn'] = conn
    temp['adress'] = addr
    temp['name'] = conn.recv(200)
    BroadcastPresence(temp)
    ListAllUser(conn)
    arr += [temp]
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    start_new_thread(clientthread, (conn,))
s.close()
