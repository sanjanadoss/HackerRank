#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        whole_range = set(range(1, len(nums)+1))
        nums = set(nums)
        diff = list(whole_range.difference(nums))
        return diff

#Runtime: 634 ms, faster than 18.79% of Python3 online submissions for Find All Numbers Disappeared in an Array.
#Memory Usage: 26.3 MB, less than 7.42% of Python3 online submissions for Find All Numbers Disappeared in an Array.