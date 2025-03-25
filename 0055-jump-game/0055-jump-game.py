'''
# Jump Game
- each element represent how many indices that you can jump ahead.
- check the possible jump cases for each time.

how can we know, we didn't reached the end when iteration is over? 
=> tracking the farthest index. if farthest index is not length-1 of the nums array? you didn't jumped to the end.
=> we can find out that we got stuck, before iterate the whole array, by checking current index is greater than maxReach. -> if we are passing the point that maxReach can reach? The end is not reachable.

during the iteration
- you can jump under current value. but, we don't need to do nested loop to solve it.
- check the next moves, pickup the greater value everytime. (greedy)
    - max(maxReach, i + nums[i]): move from i, by nums[i] amount
- if you reach to the end, return True.
- if the current index is greater than maxReach, there's no more jumps to go on. return False.
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0

        for i in range(len(nums)):
            if i > maxReach:
                return False
            
            maxReach = max(maxReach, i + nums[i])


        return True
            

