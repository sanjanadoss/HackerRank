#https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return (False if len(list(set(nums))) == len(nums) else True)


#Runtime: 528 ms, faster than 65.36% of Python3 online submissions for Contains Duplicate.
#Memory Usage: 26.1 MB, less than 5.86% of Python3 online submissions for Contains Duplicate.