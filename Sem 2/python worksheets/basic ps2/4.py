n = []
l = int(input("Enter set limit: "))
for i in range(0,l):
    s = int(input("Enter a number"))
    n.append(s)
print ("Maximum: ", max(n))
print ("Minimum: ", min(n))