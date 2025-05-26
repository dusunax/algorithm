'''
problem
- find the int that doesn't exist on other array.

approach
- we dont checkout the index for making answer array.
- 각 중복 제거된 집합을 구하고, 각 배열에만 있는 원소를 구한다.

집합
- 차집합: -
- 합집합: |
- 교집합: &
- 대칭차집합: ^
'''
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        uniqueNums1 = set(nums1)
        uniqueNums2 = set(nums2)

        diff1 = list(uniqueNums1 - uniqueNums2)
        diff2 = list(uniqueNums2 - uniqueNums1)

        return [diff1, diff2]

