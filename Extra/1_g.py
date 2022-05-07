n = int(input())
sum,i = 0, 0
while i<=n:
    if i%2==0:
        sum = sum + i
    i = i+1
print(sum)