import socket
import threading

# Set the host and port to connect to
host = '127.0.0.1'  # localhost
port = 12345

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Function to send messages to the server
def send_messages():
    while True:
        message = input("You: ")
        client_socket.send(message.encode('utf-8'))

# Start a new thread to handle sending messages
send_thread = threading.Thread(target=send_messages)
send_thread.start()

# Receive and print messages from the server
while True:
    message = client_socket.recv(1024).decode('utf-8')
    print(message)
