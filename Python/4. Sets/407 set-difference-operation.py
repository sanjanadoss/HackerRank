#https://www.hackerrank.com/challenges/py-set-difference-operation/problem

a,b = (int(input()), input().split())
c,d = (int(input()), input().split())

b,d = set(b), set(d)
x = b.difference(d)
print(len(x))
