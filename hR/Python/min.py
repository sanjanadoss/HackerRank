import math
import os
import random
import re
import sys
            
def lilysHomework(input_arr):
   pos = sorted(list(enumerate(input_arr)), key=lambda x: x[1])
   print(pos)
   count = 0

   for index in range(len(input_arr)):
      while True:
         if (pos[index][0] == index):
            break
         else:
            count += 1
            swap_index = pos[index][0]
            pos[index], pos[swap_index] = pos[swap_index], pos[index]

   return count

def solve(input_arr):
   return min(lilysHomework(input_arr), lilysHomework(input_arr[::-1]))

if __name__=='__main__':
    arr = [6,3,5,4]
    result = solve(arr)
    print(result)