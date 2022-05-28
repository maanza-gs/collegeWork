def tcfCalc(f):
    Fi=0
    for i in f:
        Fi = Fi+i
    tcf = 0.65 + 0.01*Fi
    return tcf

aSimp = int(input("Enter no. of simple external inputs:"))
aAvg = int(input("Enter no. of average external inputs:"))
aComp = int(input("Enter no. of complex external inputs:"))
bSimp = int(input("Enter no. of simple external outputs:"))
bAvg = int(input("Enter no. of average external outputs:"))
bComp = int(input("Enter no. of complex external outputs:"))
cSimp = int(input("Enter no. of simple external inquiries:"))
cAvg = int(input("Enter no. of average external inquiries:"))
cComp = int(input("Enter no. of complex external inquiries:"))
dSimp = int(input("Enter no. of simple external files:"))
dAvg = int(input("Enter no. of average external files:"))
dComp = int(input("Enter no. of complex external files:"))
eSimp = int(input("Enter no. of simple internal files:"))
eAvg = int(input("Enter no. of average internal files:"))
eComp = int(input("Enter no. of complex internal files:"))

ufc = aSimp*3+aAvg*4+aComp*6+bSimp*4+bAvg*5+bComp*7+cSimp*3+cAvg*4+cComp*6+dSimp*7+dAvg*10+dComp*15+eSimp*5+eAvg*7+eComp*10
f = []
print("Enter the factor value:")
for i in range(0,14):
    x = int(input("F: "))
    f.append(x)
    
tcf = tcfCalc(f)
fp = tcf*ufc
print("Function Point: ", fp)



    
