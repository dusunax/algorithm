class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        Iterative
        '''
        # nums.sort()
        # n = len(nums)
        
        # for i in range(n):
        #     if nums[i] != i:
        #         return i

        # return n
        '''
        XOR
        '''
        n = len(nums)
        xor_all = 0
        xor_nums = 0

        for i in range(n + 1):
            xor_all ^= i
        
        for num in nums:
            xor_nums ^= num

        return xor_all^xor_nums