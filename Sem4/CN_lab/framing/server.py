import socket
s = socket.socket()
host = socket.gethostname()
print(host)
port = 1234
s.bind((host,port))

while True:
    c,addr = s.accept()
    print ('Got connection from', addr)
    c.send(b'Thank you for connecting')
    c.close()