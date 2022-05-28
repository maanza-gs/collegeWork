s = []
n = int(input("Enter limit: "))
for i in range(0,n):
    x = int(input("Enter a number: "))
    s.append(x)
print (s)
amin = min(s)
amax = max(s)
for i, v in enumerate(s):
    s[i] = (v - amin)/(amax - amin)
print (s)