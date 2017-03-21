from socket import *

serverPortIN = 12000

serverPortOUT = 13000

serverName = 'localhost'

serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('',serverPortIN))

serverSocket.listen(1)

serverSocket1 = socket(AF_INET,SOCK_STREAM)

serverSocket1.bind(('',serverPortOUT))

serverSocket1.listen(1)

print 'The server is ready to receive'

while 1:

	connectionSocket, addr = serverSocket.accept()

	sentence = connectionSocket.recv(1024)

	capitalizedSentence = sentence.upper()
	connectionSocket1, addr = serverSocket1.accept()

	connectionSocket.send(capitalizedSentence)
	connectionSocket1.send(capitalizedSentence)
	print capitalizedSentence
	connectionSocket.close()
		connectionSocket1.close()
