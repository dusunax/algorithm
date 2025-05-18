'''
Key constraints:
- move zeros to the end of the list
- stable, in place => insertion sort => Nope, because it's O(n²)
- use pointer
'''
class Solution:
    '''
    ### Overwrite+Fill
    TC: O(n)
    SC: O(1)

    key point
    - use `write` pointer to overwrite el
    - after swaping, fills the ramaining tail with 0
    '''
    # def moveZeroes(self, nums: List[int]) -> None:
    def moveZeroesOverwrite(self, nums: List[int]) -> None:
        write = 0

        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1
        
        for i in range(write, len(nums)):
            nums[i] = 0

    '''
    ### In-Place Swap 
    TC: O(n)
    SC: O(1)

    key point
    - move in place, no two pass.
    '''
    # def moveZeroesInPlaceSwap(self, nums: List[int]) -> None:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        for read in range(len(nums)):
            if nums[read] is not 0:
                if read != write:
                    nums[write], nums[read] = nums[read], nums[write]
                write += 1