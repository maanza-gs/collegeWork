import socket

def bitstuff(sig):
    onec = 0  # one counter
    c = 0   # index counter
    one = []  # one indexes
    s = list(sig)
    for i in s:
        c += 1
        if i == '0':
            onec = 0
        else:
            onec += 1
        if onec == 5:
            one.append(c)
            onec = 0
    k = 0  # count extra index number
    for i in one:
        # print(i)
        s.insert(i + k, '0')
        k += 1
    return s


# destuffing the stuffed signal
def bitdestuff(sig):
    onec = 0  # one counter
    c = 0   # index counter
    one = []  # one indexes
    sig = list(sig)
    for i in sig:
        c += 1
        if i == '0':
            onec = 0
        else:
            onec += 1
        if onec == 5:
            one.append(c)
            onec = 0
    k = 0  # count extra index number
    for i in one:
        # print(i)
        sig.pop(i + k)
        k -= 1
    return sig


# ******************** Driver Code ************************* #

s = socket.socket()
host = socket.gethostname()
port = 12345
print(host)
s.connect((host, port))
print(s.recv(1024).decode())

sig = input("Enter the message: ")

print("Original Signal : ", sig)

stf = bitstuff(sig.encode('utf-8'))
print("Stuffed Signal : ", end="")
res = ''.join(chr(int(i)) for i in stf)
print (str(res))

dstf = bitdestuff(stf)
print("Destuffed Signal : ", end="")
res = ''.join(chr(int(i)) for i in dstf)
print (str(res))


s.close()