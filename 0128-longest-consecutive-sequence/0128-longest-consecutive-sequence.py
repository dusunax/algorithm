class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) # O(n)
        longest_sequence = 0

        for num in nums_set: # O(n)
            if (num - 1) not in nums_set:
                current_num = num
                current_sequence = 1
            
                while current_num + 1 in nums_set: # O(1) 
                    current_num += 1
                    current_sequence += 1

                longest_sequence = max(current_sequence, longest_sequence)

        return longest_sequence
