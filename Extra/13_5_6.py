#write a program to count total even and odd numbers in an array

x = list(map(int, input().split()))
ce, co = 0,0 
for i in range(len(x)):
    if x[i]%2==0:
        ce += 1
    else:
        co += 1
print(ce, co)

