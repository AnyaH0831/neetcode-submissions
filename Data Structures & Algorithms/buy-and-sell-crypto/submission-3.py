class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minP = prices[0]
        maxProfit = 0

        for r in range(1, len(prices)):

            maxProfit = max(maxProfit,prices[r] - minP)
            minP = min(minP, prices[r])

        return maxProfit