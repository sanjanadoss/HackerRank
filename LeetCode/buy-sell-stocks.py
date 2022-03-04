#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        maxp = 0
        minp = prices[0]
        for p in prices[1:]:		
            maxp = max(maxp, p - minp)
            minp = min(minp, p)

        return maxp

#Runtime: 1674 ms, faster than 31.71% of Python3 online submissions for Best Time to Buy and Sell Stock.
#Memory Usage: 25 MB, less than 57.47% of Python3 online submissions for Best Time to Buy and Sell Stock.