def hammingcode():
    d=input("Enter the signal: ")
    data=list(d)
    data.reverse()
    r=0
    c=0
    h=[]
    j=0
    ch=0
    while(len(d)+r+1)>2**r:
        r=r+1
        
    for i in range(0,r+len(d)):
        p=2**c
        
        if(p==i-1):
            h.append(0)
            c=c+1
        else:
            h.append(int(data[j]))
            j=j+1
    
    for parity in range(0, len(h)):
        ph = (2**ch)
        if ph==parity+1:
            startIndex = ph-1
            i=startIndex
            toXOR = []
            
        while i<len(h):
            block=h[i:i+ph]
            toXOR.extend(block)
            i=i+2*ph
            
        for z in range(1,len(toXOR)):
            h[startIndex]=h[startIndex]^toXOR[z]
            
        ch+=1

    h.reverse()
    print("Hamming code =", h)

#finding the error bit
def errorCorrection():
    print('Enter the hamming code received')
    d=input()
    data=list(d)
    data.reverse()
    c,ch,error,h,parity_list,h_copy=0,0,0,[],[],[]

    for k in range(0,len(data)):
        p=(2**c)
        h.append(int(data[k]))
        h_copy.append(data[k])
        if(p==(k+1)):
            c=c+1
            
    for parity in range(0,(len(h))):
        ph=(2**ch)
        if(ph==(parity+1)):

            startIndex=ph-1
            i=startIndex
            toXor=[]

            while(i<len(h)):
                block=h[i:i+ph]
                toXor.extend(block)
                i+=2*ph

            for z in range(1,len(toXor)):
                h[startIndex]=h[startIndex]^toXor[z]
            parity_list.append(h[parity])
            ch+=1
    parity_list.reverse()
    error=sum(int(parity_list) * (2 ** i) for i, parity_list in enumerate(parity_list[::-1]))
    
    if((error)==0):
        print('There is no error in the hamming code received')

    else:
        print('Error is in',error,'bit')
        
        #correcting the error
        if(h_copy[error-1]=='0'):
            h_copy[error-1]='1'

        elif(h_copy[error-1]=='1'):
            h_copy[error-1]='0'
            print('After correction hamming code is:- ')
        print(h_copy)
    
#main 
errorCorrection()