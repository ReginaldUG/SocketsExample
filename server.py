import socket

    #GET YOUR ip USING THIS METHOD
''' #NOTE: THIS WOULD GET YOUR VIRTUAL BOX IP IF YOU ARE ON VIRTUAL BOX
host = socket.gethostbyname(socket.gethostname())
print(host)
'''

    #bind the socket to a host/ip
HOST = '192.168.43.81'      #insert your own local ip address
PORT = 9090         #NOTE: DO NOT USE A RESERVED PORT NO LIKE 80 etc

    #socket.AR_INET is the type of socket connection, in this case an internet socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_STREAM is a tcp connection
socket.bind((HOST, PORT))

#listen for incoming connections
socket.listen(5)


    #accept connections
#NOTE YOU CANNOT COMMUNICATE WITH THE CLIENT VIA THE SERVER SOCKET, COMMUNICATION IS THROUGH THE COMMUNICATION CLIENT
while True:
    communication_socket, address = socket .accept()     #server.accept() returns address of connecting client and socket we can use to talk to the client
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client: {message}")
    communication_socket.send(f"Got message from client".encode('utf-8'))       #we need to encode the message cause we send bytes and not strings
    communication_socket.close()
    #print(f"Connection with client {address} ended!")


