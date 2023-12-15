import socket
import threading

# Set the host and port for the server
host = '127.0.0.1'  # localhost
port = 12345

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the specified address and port
server_socket.bind((host, port))

# Listen for incoming connections (up to 5 clients in the queue)
server_socket.listen(5)

print(f"Server listening on {host}:{port}")

# List to keep track of connected clients
clients = []

# Function to handle messages from a client
def handle_client(client_socket, client_address):
    while True:
        # Receive a message from the client
        message = client_socket.recv(1024).decode('utf-8')

        # Broadcast the message to all connected clients
        for c in clients:
            if c != client_socket:
                c.send(f"{client_address[0]}:{client_address[1]} says: {message}".encode('utf-8'))

        # If the client disconnects, remove it from the list and break the loop
        if not message:
            clients.remove(client_socket)
            break

# Accept and handle incoming connections
while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)

    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
