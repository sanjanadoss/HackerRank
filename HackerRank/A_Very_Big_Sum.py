import sys
N=int(input())
k=list()
val=list()
sum = 0 
if (N<1 or N>10):
     sys.exit("enter value b/w 1,10")
val=list(map(int,input().split(" ")))
for i in range (0,N):         
     if (int (max (val))>10000000000 or int(min (val))<0):             
         sys.exit("enter value b/w 0,10^2")
     sum = sum+int(val[i])
     
print(sum)
