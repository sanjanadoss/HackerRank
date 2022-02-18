#https://www.hackerrank.com/challenges/polar-coordinates/problem

import cmath
x = complex(input().strip())
print(cmath.polar(x)[0])
print(cmath.polar(x)[1])