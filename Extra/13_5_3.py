#write a program to find sum of all array elements

x = list(map(int, input().split()))
print(sum(x[i] for i in range(len(x))))