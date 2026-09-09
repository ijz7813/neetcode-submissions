class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxprofit = 0 
        while r < len(prices):
            if prices[r]>prices[l]:
                currprofit = prices[r]-prices[l]
                maxprofit = max(maxprofit, currprofit)
            else:
                l=r
            r+=1
        
        return maxprofit

