'''
Key constraints:
- move zeros to the end of the list
- stable, in place => insertion sort

insert sort
- sorted array
- pick up the target from unsorted array, iterate sorted array for comparsion, find the right place? insert it.

key point
- use write to overwrite el
- after swapping, fills the ramaining tail with 0
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0

        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1
        
        for i in range(write, len(nums)):
            nums[i] = 0

        # last_non_zero_at = 0
        # for current in range(len(nums)):
        #     if nums[current] is not 0:
        #         nums[last_non_zero_at], nums[current] = nums[current], nums[last_non_zero_at]
        #         last_non_zero_at += 1