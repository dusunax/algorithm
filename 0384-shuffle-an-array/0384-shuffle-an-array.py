class Solution:
    def __init__(self, nums: List[int]):
        self.array = nums    
        self.origin = nums

    def reset(self) -> List[int]:
        self.array = self.origin
        return self.origin

    def shuffle(self) -> List[int]:
        temp = []
        unique_indices = set()

        while len(temp) < len(self.array):
            idx = random.randint(0, len(self.array) - 1)
            if idx not in unique_indices:
                temp.append(self.array[idx])
                unique_indices.add(idx)

        self.array = temp
        return self.array
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()