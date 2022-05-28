#Q1
library(lpSolve)
f.obj <- c(30, 20)
f.con <- matrix(c(2, 1, 1, 3), nrow = 2, byrow = TRUE)
f.dir <- c("<=","<=")
f.rhs <- c(8,8)
lp("max", f.obj, f.con, f.dir, f.rhs)
lp("max", f.obj, f.con, f.dir, f.rhs) $solution

#Question 1: If JOBCO can increase the capacity of both machines, which machine should
receive higher priority?
print("Q1")
dcons<-lp("max", f.obj, f.con, f.dir, f.rhs, compute.sens=TRUE)$duals
if (dcons[1]>dcons[2]){
print("Machine 1 should receive high priority")
}else{
print("Machine 2 should receive high priority")
}

#Question 2. A suggestion is made to increase the capacities of machines 1 and 2 at theadditional cost of $10/hr. Is this advisable?NetRev1=dcons[1]-10
print("Q2")
NetRev2=dcons[2]-10
if (NetRev1>0){
print("Increase capacity of MAchine 1 is advisable")
}else{
print("Increasing capacity of Machine 1 is not advisable")
}
if (NetRev2>0){
print("Increase capacity of MAchine 2 is advisable")
}else{
print("Increasing capacity of Machine 2 is not advisable")
} 

#Question 3. If the capacity of machine 1 is increased from the present 8 hours to 13 hours,
#how will this increase impact the optimum revenue?
print("Q3")
dfrom<-lp("max", f.obj, f.con, f.dir, f.rhs, compute.sens=TRUE)$duals.from
dto<-lp("max", f.obj, f.con, f.dir, f.rhs, compute.sens=TRUE)$duals.to
New_Const_Mach1=13
if((New_Const_Mach1>=dfrom[1])&&(New_Const_Mach1<=dto[1]))
{
print("Increase is possible")
incr=dcons[1]*(New_Const_Mach1-f.rhs[1])
cat("Increase in Revenue is ", incr)
cat("\nTotoal optimum value is", incr+z)
}else{
print("Increase is not possible")
}

#Question 4. Suppose that the capacity of machine 1 is increased to 20 hours,
#hQW will this increase impact the optimum revenue?
print("Q4")
New_Const_Mach1=20
if((New_Const_Mach1>=dfrom[1])&&(New_Const_Mach1<=dto[1]))
{
print("Increase is possible")
incr=dcons[1]*(New_Const_Mach1-f.rhs[1])
cat("Increase in Revenue is ", incr)
cat("\nTotoal optimum value is", incr+z)
}else{
print("Increase is not possible")
}


#Question 5. Suppose that the unit revenues for products 1 and 2 are changed to $35 and $25,
#respectively. Will the current optimum remain the same?
print("Q5")
objfrom<-lp("max", f.obj, f.con, f.dir, f.rhs, compute.sens=TRUE)$sens.coef.from
objto<-lp("max", f.obj, f.con, f.dir, f.rhs, compute.sens=TRUE)$sens.coef.to
f.obj[1]=35
if((f.obj[1]>=objfrom[1])&&(f.obj[1]<=objto[1])){
print("Changes in objective coefficient 1 feasible")
print("No changes in solution")
cat("Solution remains same",dcons[1],dcons[2])
Newopt<-lp("max", f.obj, f.con, f.dir, f.rhs)
Newz<-Newopt$objval
cat("\nHowever New optimum value is",Newz)
cat("\n")
}else{
print("We have to Reframe the LPP")
}

f.obj[2]=25
if((f.obj[2]>=objfrom[2])&&(f.obj[2]<=objto[2])){
print("Changes in objective coefficient 2 feasible")
print("No changes in solution")
cat("Solution remains same",dcons[1],dcons[2])
Newopt1<-lp("max", f.obj, f.con, f.dir, f.rhs)
Newz1<-Newopt1$objval
cat("\nHowever New optimum value is",Newz1)
}else{
print("We have to Reframe the LPP")
}