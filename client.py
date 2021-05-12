import socket
import time
# import random


def print_time(newline):
	current_time = time.localtime()
	if newline:
		print(f"\n[{time.strftime('%H:%M:%S', current_time)}]", end=" ")
	else:
		print(f"[{time.strftime('%H:%M:%S', current_time)}]", end=" ")


quitFlag = False

# creating basic socket connection to server
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print_time(0)
print("Client starting up...")

while not quitFlag:
	print_time(1)
	print("Please type the message you would like to send below, or q to quit:\n")
	message = input()

	if len(message) >= 65:
		print_time(0)
		print(f"Message is {len(message)} characters long! Please send a message 64 characters or less in length.\n")
	elif message == "q":
		# need to send quit message to the server before powering down
		client.sendto(str.encode(message), ('127.0.0.1', 1337))
		print_time(1)
		print("Quit message received, powering down!\n")
		quitFlag = True
	else:
		client.sendto(str.encode(message), ('127.0.0.1', 1337))
# cleanup
client.close()