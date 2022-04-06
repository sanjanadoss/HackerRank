#https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res, i = 0, 0
        for i in range(len(s)):
            i, j = s[i], s[i+1:i+2]
            if j and roman[i] < roman[j]:
                res -= roman[i]
            else:
                res += roman[i]
        return res
        
#Runtime: 46 ms, faster than 91.64% of Python3 online submissions for Roman to Integer.
#Memory Usage: 13.9 MB, less than 34.17% of Python3 online submissions for Roman to Integer.