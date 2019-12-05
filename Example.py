import socket
 
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
 
s.bind(("localhost",8888))
 
s.listen(10)
 
while 1:
   connection, address = s.accept()
   message             = connection.recv(1024)
   print "Got: {0}".format(message)
   #connection.send("Message received\n")
   connection.close()

