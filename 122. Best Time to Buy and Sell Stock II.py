#  https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                diff += prices[i] - prices[i-1]
                
        return diff
        
