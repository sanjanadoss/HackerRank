#https://leetcode.com/problems/running-sum-of-1d-array/

#O(n) – time complexity
#O(1) – space 
def runningSum(self, nums: List[int]) -> List[int]:
    sum = 0
    i = 0
    for i in range(0, len(nums)):
        sum += nums[i]
        nums[i] = sum
    return nums
