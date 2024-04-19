# SERVER THAT CAN HANDLE MULTIPLE STREAMS OF INFORMATION
import socket
import threading

# Function to handle client connection
def handle_client(client_socket, address):
    print(f"Connected to {address}")

    while True:
        try:

            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Message received from client {address}: {message}")
            response = "Got message from client"
            client_socket.send(response.encode('utf-8'))

        except ConnectionResetError:

            print(f"Connection with client {address} was forcibly closed")
            break

    client_socket.close()
    print(f"Communication with Client {address} ended")

# server configuration
HOST = '192.168.43.81'
PORT = 9090

# create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Server is listening on {HOST}:{PORT}")

# Loop to accept incoming connections
while True:
    client_socket, address = server_socket.accept()
    # thread to handle client connection
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()