class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        for i in range(len(prices)):
            if min_price < prices[i]:
                profit = max(profit,prices[i]-min_price)
            else :
                min_price = prices[i]
        return profit
                
            
        