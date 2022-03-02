#https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        x = []
        if len(original) == m*n: 
            for i in range(0, len(original), n): 
                x.append(original[i:i+n])
        return x 

#Runtime: 1363 ms, faster than 50.15% of Python3 online submissions for Convert 1D Array Into 2D Array.
#Memory Usage: 21.3 MB, less than 87.00% of Python3 online submissions for Convert 1D Array Into 2D Array.