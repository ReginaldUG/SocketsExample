import socket

#Specify the IP of the server, since its run on the same computer it will be the same ip as the computer
HOST = '192.168.43.81'
PORT = 9090     #port has to be the same as sevrer

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#since we are connecting we call the connect function
socket.connect((HOST,PORT))

socket.send("Hello World".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))
