#https://www.hackerrank.com/challenges/py-set-union/problem

a,b = (int(input()), input().split())
c,d = (int(input()), input().split())

b,d = set(b), set(d)
x = b.union(d)
print(len(x)) 