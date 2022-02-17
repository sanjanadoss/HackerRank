import math
import os
import random
import re
import sys

n = int(input())
arr = list(map(int, input().strip().split(' ')))
length = len(arr)

flag = 0
flag2 = 0
flag3 = 0
for i in range(length):
    if (arr[i]<0):
        flag = flag + 1
    if (arr[i]>0) :
        flag2 = flag2 + 1
    if (arr[i]==0):
        flag3 = flag3 +1


flag2 = flag2/n
print ('%.6f'%flag2)
flag = flag/n
print ('%.6f'%flag)
flag3 = flag3/n
print ('%.6f'%flag3)
    