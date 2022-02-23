#https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

a,b = (int(input()), input().split())
c,d = (int(input()), input().split())

b,d = set(b), set(d)
x = b.symmetric_difference(d)
print(len(x))