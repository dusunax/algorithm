class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        # for i in range(len(prices)):
        #     if min_price > prices[i]:
        #         min_price = prices[i]
        #     max_profit = max(prices[i] - min_price, max_profit)

        for p in prices[1:]:
            if min_price > p:
                min_price = p
            max_profit = max(p - min_price, max_profit)
            
        
        return max_profit