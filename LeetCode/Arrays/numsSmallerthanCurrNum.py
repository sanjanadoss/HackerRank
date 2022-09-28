#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/

def smallerNumbersThanCurrent(self, nums):
    """
    Time: O(n log n) because of sort. Space: O(n) bcoz of dictionary.
    """
    temp = sorted(nums)
    num_dict = {}
    result = []
    for i in range(len(temp)):
        #[8,1,2,2,3]
        #[1,2,2,3,8]
        if temp[i] not in num_dict:
            num_dict[temp[i]] = i
    for i in nums:
        result.append(num_dict[i])
    return result