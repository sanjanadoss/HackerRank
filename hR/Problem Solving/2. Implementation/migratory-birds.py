#https://www.hackerrank.com/challenges/migratory-birds/problem

input()
count = [0]*6
for t in map(int,input().strip().split()):
    count[t] += 1
print(count.index(max(count)))