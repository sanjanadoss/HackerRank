#https://leetcode.com/problems/move-zeroes/


temp = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[temp], nums[i] = nums[i], nums[temp]
        temp += 1
