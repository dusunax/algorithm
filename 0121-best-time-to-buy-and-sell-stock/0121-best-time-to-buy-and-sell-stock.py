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
        # is there's a base case??
        if len(prices) == 1:
            return 0
        
        # two pointers
        lowest_price = prices[0]
        max_profit = 0
        
        for price in prices:
            lowest_price = min(price, lowest_price)
            curr_profit = price - lowest_price
            max_profit = max(curr_profit, max_profit)
        
        return max_profit