# dp to solve climbing stairs
# do we have to save the nth index's sums? yes

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        sums = [-1] * (len(cost) + 1) # dp table for sums of each indices
        
        def dp(i: int):
            if i <= 1: 
                return 0
            if sums[i] != -1:
                return sums[i] # pick it up the memoed result
            
            sums[i] = min(
                dp(i - 1) + cost[i - 1], 
                # dp(i-1) is the memoed result of min cost we add up before
                # cost[i-1] is cost that we are going to step on it
                dp(i - 2) + cost[i - 2]
            ) 
            return sums[i]

        return dp(len(cost))
        