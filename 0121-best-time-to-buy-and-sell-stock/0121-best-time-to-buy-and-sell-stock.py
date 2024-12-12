'''
# 121. Best Time to Buy and Sell Stock

use **bottom-up dynamic programming** to solve the problem.

## Time and Space Complexity
```
TC: O(n)
SC: O(1)
```

## TC is O(n):
- iterating through the list just once to find the maximum profit. = O(n)

## SC is O(1):
- using two variables to store the minimum price and maximum profit. = O(1)
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            max_profit = max(prices[i] - min_price, max_profit)
        
        return max_profit