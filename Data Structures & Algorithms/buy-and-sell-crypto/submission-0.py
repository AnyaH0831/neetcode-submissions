class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        stack = {prices[0]}

        for i in range(1,len(prices)):

            if prices[i] - min(stack) > maxProfit:
                maxProfit = prices[i] - min(stack)
            
            stack.add(prices[i])

        return maxProfit

