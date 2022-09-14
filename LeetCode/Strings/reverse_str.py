#https://leetcode.com/problems/reverse-string/

def reverseString(self, s):
    """
    we go from the start and the end of the string and swap pair of elements. 
    One thing, that we need to do is to stop at the middle of our string. 
    We can see this as simplified version of two points approach, 
    because each step we increase one of them and decrease another.
    """
    
    ll = 0
    rr = len(s) - 1
    while ll < rr:
        s[ll], s[rr] = s[rr], s[ll]
        ll += 1
        rr -= 1