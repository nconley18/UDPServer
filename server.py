import socket
# import threading

PORT = 1337
IP = "127.0.0.1"

ADDR = (IP, PORT)

# create server socket and bind it to the pre-defined IP and port
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Server starting up...\n")
server.bind(ADDR)

# basic infinite loop to receive data from the sender
try:
    print("Waiting to receive message.\n")
    data, addr = server.recvfrom(64)
    print(f"Received message of length {len(data)}\n")
    print(f"Message is: {str(data.decode())}")
finally:
    server.close()