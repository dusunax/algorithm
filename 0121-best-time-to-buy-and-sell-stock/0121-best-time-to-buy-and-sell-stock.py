class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            # min_price = min(prices[i], min_price)
            if min_price > prices[i]:
                min_price = prices[i]
            max_profit = max(prices[i] - min_price, max_profit)
        
        return max_profit