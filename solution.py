# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  #localHost = "127.0.0.1"  #Not needed
  serverSocket.listen(1) #listen on the socket
  #Fill in end

  while True:
    #Establish the connection
    #print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start -are you accepting connections?     #Fill in end
    
    try:
      message = connectionSocket.recv(1024) #Fill in start -a client is sending you a message   #Fill in end
      filename = message.split()[1]
      
      #opens the client requested file. 
      f = open(filename[1:]) #fill in start #fill in end)
      #fill in end
      #outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"\#
      outputdata = f.read()  # store the code in file.html to variable outputdata
      #Fill in start -This variable can store your headers you want to send for any valid or invalid request.
      #Content-Type above is an example on how to send a header as bytes
      #Fill in end

      #Send an HTTP header line into socket for a valid request. What header should be sent for a response that is ok? 
      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
      #Fill in start
      connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())  # send the HTTP header to Socket
      #Fill in end
               

      #Send the content of the requested file to the client
      num_chars = len(outputdata)
      for i in range(0, num_chars): #for line in file
        #Fill in start - send your html file contents #Fill in end
        #print(len(outputdata))
        #print(i)
        connectionSocket.send(outputdata[i].encode())
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      #Fill in start

      connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())  # If file not there then 404 NOT FOUND Error Page Header.
      connectionSocket.send(
        "<html><head></head><body><h1>404 Not Found</h1></body></html>".encode())  # HTML formatted code returning  error: 404 NOT FOUND in respone to Browser
      #print(e)
      return;

      #Fill in end


      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
