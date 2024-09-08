class Solution:
    # time: O(N)
    # space: O(N)
    # def rotate(self, nums: List[int], k: int) -> None:
    #     n = k % len(nums)

    #     new_nums = nums[-n:] 
    #     del nums[-n:] 
        
    #     nums[0:0] = new_nums 

    # 역순 기법 Reversals 
    # time: O(N)
    # space: O(1), modify array in-place
    def rotate(self, nums: List[int], k: int) -> None:
        n = k % len(nums)

        nums.reverse()
        nums[:n] = reversed(nums[:n])
        nums[n:] = reversed(nums[n:])