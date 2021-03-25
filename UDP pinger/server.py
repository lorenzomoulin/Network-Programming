from socket import *
import time
import random
# What's your IP address and witch port should we use?
recieve_host = '127.0.0.1'
recieve_port = 65000

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind((recieve_host, recieve_port))


while True:
  message, address = serverSocket.recvfrom(1024)
  message = message.upper()
  print ('Recieve: ' + str(message))
  delay = random.randint(0, 1500)
  print(delay)
    
#   time.sleep(delay / 1000)
  if delay < 1000:
    time.sleep(delay / 1000)
    serverSocket.sendto(message, address)
 