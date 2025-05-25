'''
problem
- find the int that doesn't exist on other array.

approach
- we dont checkout the index for making answer array. => conter method
'''
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1set = set(nums1)
        nums2set = set(nums2)

        only1 = list(nums1set - nums2set)
        only2 = list(nums2set - nums1set)

        return [only1, only2]

