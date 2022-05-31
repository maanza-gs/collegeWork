def xor(a,b):
    result = []
    for i in range(1,len(b)):
        if a[i]==b[i]:
            result.append('0')
        else:
            result.append('1')
    return result

def crcDiv(data, key):
    ld = len(key)
    tempD = data[0:ld]
    
    while ld<len(data):
        if tempD[0] == '1':
            tempD = xor(key,tempD) + data[ld]
        else:
            tempD = xor(0*key, tempD) + data[ld]
        ld+=1

    if tempD[0] == '1':
        tempD = xor(key,tempD)
    else:
        tempD = xor(0*key, tempD)

    print(tempD)
    for i in tempD:
        if i=='1':
            print("Error")
            break

crcDiv('1001110','1011')
