colours = []
c = 1
for i in range(0,4):
    s = input("Enter a colour: ")
    colours.append(s)
print (colours)
colours.remove("Red")
print (colours)
if "Yellow" in colours:
    print ("Yellow is present...")
else:
    print ("Yellow is not present...")