#https://leetcode.com/problems/find-all-duplicates-in-an-array/

def findDuplicates(self, nums):
    """
    A regular hash map solution would be to make a frequency table
    then return all numbers with frequency more than 1
    

    alternate hashing technique:
    use the array itself as a hash map to store information. (hashmap with O(1) space)
    Since we have indices [0, n-1] and number from [0, n-1]
    imaginary hash map form - {index: (parity of number at that index)}
    """
    
    ans = []
    """
    why num instead of i?
    because the values in the array are between 1 and n.
    When you reference nums[abs(x)-1], you are guaranteed to have a valid index. 
    Essentially the same number will reference the same index every time, 
    so the first time you get to a value/index you set it the number at that index negative. 
    The second time you get to a value/index, 
    that index will have a number that is negative so duplicate.
    """
    for num in nums:
        if nums[abs(num)-1] < 0:
            ans.append(abs(num))
        else:
            nums[abs(num)-1] *= -1
    return ans