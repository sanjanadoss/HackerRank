#https://www.hackerrank.com/challenges/py-check-subset/problem

for i in range(int(input())):
    _,a = (int(input()), set(input().split()))
    _,b = (int(input()), set(input().split()))
    print(a.issubset(b))