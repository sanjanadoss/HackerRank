#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        fin = []
        for i in range(0,len(nums)-1):
            for j in range(i+1 ,len(nums)):
                if nums[i]+nums[j]==target:
                    fin.append(i)
                    fin.append(j)
                    return fin
        
#runtime : 5719 ms (runtime beats 12.43 % of python3 submissions.)
#memory : 14.9 MB (memory usage beats 72.28 % of python3 submissions.)