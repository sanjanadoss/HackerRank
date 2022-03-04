#https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = [x for x in nums if x !=0] + [0] * nums.count(0)

#Runtime: 298 ms, faster than 31.43% of Python3 online submissions for Moves Zero.
#Memory Usage: 15.6 MB, less than 47.10% of Python3 online submissions for Moves Zero.