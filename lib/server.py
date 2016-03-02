import socket
host = ""
port = 8000
size = 1024
backlog = 5
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
while True:
	client, address = s.accept()
	data = client.recv(size)
	if data:
		client.send(data)
		client.close()

