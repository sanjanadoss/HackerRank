#https://leetcode.com/problems/jewels-and-stones/

'''
case -sensitive string characters
'''
def numJewelsInStones(self, jewels: str, stones: str) -> int:
    count=0
    for i in stones:
        if i in jewels:
            count = count + 1
    return count