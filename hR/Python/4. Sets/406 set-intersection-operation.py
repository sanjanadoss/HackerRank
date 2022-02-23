#https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

a,b = (int(input()), input().split())
c,d = (int(input()), input().split())

b,d = set(b), set(d)
x = b.intersection(d)
print(len(x))
