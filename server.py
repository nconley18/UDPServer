import socket
import time
# import threading


def print_time(newline):
    current_time = time.localtime()
    if newline:
        print(f"\n[{time.strftime('%H:%M:%S', current_time)}]", end=" ")
    else:
        print(f"[{time.strftime('%H:%M:%S', current_time)}]", end=" ")


quitFlag = False

PORT = 1337
IP = "127.0.0.1"

ADDR = (IP, PORT)

# create server socket and bind it to the pre-defined IP and port
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print_time(0)
print("Server starting up...\n")
server.bind(ADDR)

# basic infinite loop to receive data from the sender
while not quitFlag:
    print_time(0)
    print("Waiting to receive message.\n")
    data, addr = server.recvfrom(64)
    # message needs to be decoded from bytes back to a string
    message = str(data.decode())
    if message == "q":
        print_time(0)
        print("Quit message received, powering down!\n")
        quitFlag = True
    else:
        print_time(0)
        print(f"Received message of length {len(message)}\n")
        print_time(0)
        print(f"Message is: {message}\n")
server.close()