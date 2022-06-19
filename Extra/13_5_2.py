#write a program to find all the -ve numbers of an array

x = list(map(int, input().split()))

for i in range(len(x)):
    if x[i]<0: print(x[i])
