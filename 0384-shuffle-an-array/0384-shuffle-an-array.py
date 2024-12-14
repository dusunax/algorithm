class Solution:
    '''
    1. use set & while loop
    - first solution to think of.
    '''
    # def __init__(self, nums: List[int]):
    #     self.array = nums    
    #     self.origin = nums

    # def reset(self) -> List[int]:
    #     self.array = self.origin
    #     return self.origin

    # def shuffle(self) -> List[int]:
    #     temp = []
    #     unique_indices = set()

    #     while len(temp) < len(self.array):
    #         idx = random.randint(0, len(self.array) - 1)
    #         if idx not in unique_indices:
    #             temp.append(self.array[idx])
    #             unique_indices.add(idx)

    #     self.array = temp
    #     return self.array

    '''        
    2. need to use shallow copy
    - Fisher-Yates shuffle will do TC: O(n), SC: no additional memory
    '''
    # def __init__(self, nums: List[int]):
    #     self.array = nums[:]
    #     self.origin = nums[:]

    # def reset(self) -> List[int]:
    #     self.array = self.origin[:]
    #     return self.origin

    # def shuffle(self) -> List[int]:
    #     for i in range(len(self.array) - 1, 0, -1):
    #         j = random.randint(0, i)
    #         self.array[i], self.array[j] = self.array[j], self.array[i]
    #     return self.array

    '''
    3. use random
    '''
    def __init__(self, nums: List[int]):
        self.array = nums[:]
        self.origin = nums[:]

    def reset(self) -> List[int]:
        self.array = self.origin[:]
        return self.origin

    def shuffle(self) -> List[int]:
        '''
        3-1. random.shuffle is shuffle array in place
        '''
        shuffled = self.array[:]
        random.shuffle(shuffled)
        self.array = shuffled
        return self.array
        
        '''
        3-2. random.sample make a new array
        '''
        # shuffled = random.sample(self.array, len(self.array))
        # self.array = shuffled
        # return self.array

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()