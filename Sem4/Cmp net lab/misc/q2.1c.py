import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddr = ('localhost', 1234)
s.sendto(bytes("Hello!", "utf-8"), serverAddr)
while True:
    filename = 'skz.txt'
    f = open(filename, 'r')
    data = f.read(1024)
    while (data):
        s.sendto(bytes(data,"utf-8"), serverAddr)
        print('File sent', repr(data))
        data = f.read(1024)
    f.close()
    
    print("File Sent")
    s.sendto(bytes("Thank you for connecting", "utf-8"), serverAddr)
    s.close()