#https://leetcode.com/problems/sort-even-and-odd-indices-independently/
def sortEvenOdd(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums[::2] = sorted(nums[::2])
    nums[1::2] = sorted(nums[1::2], reverse=True)
    return nums