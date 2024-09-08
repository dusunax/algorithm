class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = k % len(nums)

        new_nums = nums[-n:] 
        del nums[-n:] 
        
        nums[0:0] = new_nums 