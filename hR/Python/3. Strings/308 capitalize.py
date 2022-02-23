#https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
    return " ".join([ss.capitalize() for ss in s.split(" ")])