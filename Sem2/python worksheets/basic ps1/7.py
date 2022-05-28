alphabets = ["a b c d e f g h i j k l m n o p q r s t u v w x y z"]
c = 1
s = input("Enter a string: ")
s.split()
print (s)
for i in s:
    if i not in alphabets:
        c = 0
        break
if c==0:
    print ("String is not a panagram")
else:
    print ("string is a panagram")