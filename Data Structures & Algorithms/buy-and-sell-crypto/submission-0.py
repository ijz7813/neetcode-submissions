class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0

        left, right = 0, 1
        while right < len(prices):
            if prices[left] < prices[right]:
                currprofit = prices[right]-prices[left]
                maxprofit = max(currprofit,maxprofit)
            else:
                left = right
            right+=1
        
        return maxprofit
