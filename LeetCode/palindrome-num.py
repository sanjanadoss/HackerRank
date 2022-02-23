#https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = str(x)[::-1]
        if x==y:
            return True
        else:
            return False

#Runtime: 104 ms (runtime beats 34.27 % of python3 submissions.)
#Memory Usage: 13.9 MB (memory usage beats 64.33 % of python3 submissions.)