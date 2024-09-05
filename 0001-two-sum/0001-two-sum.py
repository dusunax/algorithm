# // \U0001f449 One-pass Hash Table
# // Time complexity: O(n)
# // Space complexity: O(n)
# var twoSum = function(nums, target) {
#     const map = new Map();
#     for (let i = 0; i < nums.length; i++) {    
#         const pairNum = target - nums[i];
#         if(map.has(pairNum)) {
#             return [map.get(pairNum), i]
#         }
#         map.set(nums[i], i)
#     }
# };

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}       
        for i in range(len(nums)):
            pairNum = target - nums[i]
            if map.get(pairNum) is not None:
                return [map.get(pairNum), i]
            map[nums[i]] = i
            