#https://leetcode.com/problems/length-of-last-word/

'''O(n) complexity and O(1) space

    1. find the last element of last word: traverse from the end and find first non-space   symbol.
    2. continue traverse and find first space symbol (or beginning of string)
    3. return end - begin. '''
    
def lengthOfLastWord(self, s):
    
    end = len(s) - 1
    while end > 0 and s[end] == " ": 
        end -= 1
    begin = end
    while begin >= 0 and s[begin] != " ": 
        begin -= 1
        
    return end - begin