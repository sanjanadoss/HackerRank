#https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i<len(nums):
            if i==len(nums)-1:
                return (nums[len(nums)-1])
            else:
                if nums[i]!=nums[i+1]:
                    return (nums[i])
            i = i+2

#Runtime: 149 ms, faster than 76.11% of Python3 online submissions for Single Number.
#Memory Usage: 16.9 MB, less than 15.89% of Python3 online submissions for Single Number.