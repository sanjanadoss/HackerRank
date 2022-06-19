#write a program to count all negative nos. in an array

x = list(map(int, input().split()))
c = 0
for i in range(len(x)):
    if x[i]<1: print(x[i])
