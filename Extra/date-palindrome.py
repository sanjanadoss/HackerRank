# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 14:56:43 2022

@author: Sanjana
"""
#input will be of the form dd.mm.yy

date = input()
x = date.split(".")
x = ''.join(x)
print(x)
y = str(x)[::-1]
print(y)
if x==y:
    print("yes")
else:
    print("no")
