#https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

x = int(input())
print(is_leap(x))