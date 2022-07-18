
from socket import *
from time import time, ctime
import sys

msgFromClient       = "Hello UDP Server"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("ec2-3-6-93-42.ap-south-1.compute.amazonaws.com", 11023)

UDPClientSocket = socket(family=AF_INET, type=SOCK_DGRAM)

UDPClientSocket.settimeout(1)
for i in range(10):
    startTime = time()
    message = "Ping " + str(i+1) + " " + ctime(startTime)[11:19]

    try:
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        encodedModified, serverAddress = UDPClientSocket.recvfrom(bufferSize)
        endTime = time()
        modifiedMessage = encodedModified.decode()
        print(modifiedMessage)
        print("Overall delay: %.3f ms\n" % ((endTime - startTime)*1000))
    except:
        print("PING %i Request timed out\n" % (i+1))

UDPClientSocket.close()
