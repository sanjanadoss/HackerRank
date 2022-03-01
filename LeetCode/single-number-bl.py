#using XOR 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0
        for i in nums:
            n ^= i
        return n
#Runtime: 132 ms, faster than 93.16% of Python3 online submissions for Single Number.
#Memory Usage: 16.8 MB, less than 15.89% of Python3 online submissions for Single Number.

#using sets
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums))-sum(nums)


#Runtime: 191 ms, faster than 53.12% of Python3 online submissions for Single Number.
#Memory Usage: 17.1 MB, less than 7.40% of Python3 online submissions for Single Number.

