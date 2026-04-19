class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        minP = prices[0]

        for i in range(1,len(prices)):

            if prices[i] - minP > maxProfit:
                maxProfit = prices[i] - minP
            
            if prices[i] < minP:
                minP = prices[i]

        return maxProfit

