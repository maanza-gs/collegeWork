import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host,port))

while True:
    msg = input('Please enter the message to the server: ')
    s.send(msg.encode())
    reply = s.recv(1024)
    print('Server replied: ' + reply.decode())
    if reply == 'Goodbye':
        break
    
s.close()