import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 1234))
while True:
    c, addr = s.recvfrom(1024)
    print ("Got connection from", addr)
    msg = c.recvfrom(1024)
    print('Server received', repr(msg[0]))
    
    with open('received_file', 'wb') as f:
        print ('File Opened')
        while True:
            print('Receiving...')
            data = s.recvfrom(1024)
            print('data = %s', (data[0]))
            
            f.write(data[0])
        
    f.close()
    print("Received the file successfully")
s.close()