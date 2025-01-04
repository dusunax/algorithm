class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if coins[0] == amount:
            return 1

        coins.sort()
        coins.reverse()
        
        queue = deque([(amount, 0)])
        visited = set()

        while queue:
            remain, count = queue.popleft()
            print(remain, count)

            for coin in coins:
                next_remain = remain - coin

                if next_remain == 0:
                    return count + 1
                if next_remain > 0 and next_remain not in visited:
                    queue.append((next_remain, count + 1))
                    visited.add(next_remain)
    
        return -1
        # 5 => 2 => 1
        # base case: 0 => 0, 1 => coins[0] === amount