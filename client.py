import socket
import random

# creating basic socket connection to server
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Client starting up...\n")

try:
	print("Please type the message you would like to send below:\n")
	message = input()

	if len(message) >= 65:
		print(f"Message is {len(message)} characters long! Please send a message 64 characters or less in length.\n")
	else:
		client.sendto(str.encode(message), ('127.0.0.1', 1337))
finally:
	# cleanup
	client.close()