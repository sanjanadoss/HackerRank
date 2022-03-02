#https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + [0] * len(digits)
        
#Runtime: 52 ms, faster than 36.76% of Python3 online submissions for Plus One.
#Memory Usage: 13.9 MB, less than 53.67% of Python3 online submissions for Plus One.

#new logic:

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            digits[~i] = 0
        return [1] + [0] * len(digits)

#~ is ones complement. ~i gives i-th element from the back.