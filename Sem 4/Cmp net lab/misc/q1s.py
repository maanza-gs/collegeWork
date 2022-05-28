import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port))

s.listen(1)
c,addr = s.accept()
while True:
    msg = c.recv(1024).decode()
    if msg:
        if msg == 'Bye' or msg == 'bye' or msg == 'BYE':
            c.send(b'Goodbye')
        else:
            c.send(b'OK')
    else:
        c.send(b'Connection Failed')
    c.close()
    
s.close()
