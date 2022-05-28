import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
print(host)
s.connect((host, port))
print(s.recv(1024).decode())
#print(msg.decode("utf-8"))
s.close()