web = []
print ("Enter 4 website names: ")
for i in range (0,4):
    s = input("Enter: ")
    web.append(s)
for i in web:
    print(i.split(".", -1)[-1])