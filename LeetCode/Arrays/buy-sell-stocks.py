#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(self, prices):
    """
n--> length of array
Time Complexity: O(n)
Space Complexity: O(1)
sliding window is a comp. technique used to reduce the 
use of nested loops and replace it with a single loop
to reduce complexity
    """
    
    l = 0 #buy
    r = 1 #sell
    max_p = 0
    
    while r<len(prices):
        if prices[r]>prices[l]:
            profit = prices[r]-prices[l]
            max_p = max(max_p, profit)
        else:
            l = r
        r +=1