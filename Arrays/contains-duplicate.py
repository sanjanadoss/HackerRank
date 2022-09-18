#https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return (False if len(list(set(nums))) == len(nums) else True)

def containsDuplicate(self, nums):
    """
    using set instead of dict because key pair values need not be stored
    add(), append() is O(1) complexity
    
    """
    
    s = set()
    for i in nums:
        if i not in s:
            s.add(i)
        else:
            return True
    return False

#Runtime: 528 ms, faster than 65.36% of Python3 online submissions for Contains Duplicate.
#Memory Usage: 26.1 MB, less than 5.86% of Python3 online submissions for Contains Duplicate.