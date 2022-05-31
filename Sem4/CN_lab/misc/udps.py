import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost', 9999))

print('Server waiting')

while True:
    cData=s.recvfrom(1024)
    msg = cData[0]
    cIp = cData[1]
    print('Server is connected with :' ,cIp)
    print('Message from client:', msg.decode())
    s.sendto(msg,cData[1])
    
s.close()