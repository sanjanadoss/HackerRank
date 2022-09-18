#https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int: 
        n = len(nums)
        return n*(n+1)//2 - sum(nums)
                

#Runtime: 176 ms, faster than 64.34% of Python3 online submissions for Missing Number.
#Memory Usage: 15.2 MB, less than 89.95% of Python3 online submissions for Missing Number.