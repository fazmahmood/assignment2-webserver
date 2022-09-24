# import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
serverSocket.bind(('', 1337))  # I've chosen to use port '1337' which means 'leet' also elite in a way to look cool and discrete from others.
serverSocket.listen(1)  # Setting Number Of Connections that can go through to "1 connection at a time).
# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # the method to establish a new connection for the client
    try:
        message = connectionSocket.recv(1024)  # the method to receive the request from the client, 1024 is the size
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()  # store all the code in XXX.html to variable outputdata
        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())  # this method is to send the HTTP header to Socket
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())  # 404 NOT FOUND Error Page Header.
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>".encode())  # HTML formatted code returns (404 NOT FOUND) error based respone to Browser.
        # Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

serverSocket.close()
