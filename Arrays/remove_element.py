#https://leetcode.com/problems/remove-element/

def removeElement(self, nums, val):
        x = 0
        for i in range(len(nums)):
            if(nums[i]!=val):
                nums[x] = nums[i]
                x+=1
        print(nums)
        return(x)