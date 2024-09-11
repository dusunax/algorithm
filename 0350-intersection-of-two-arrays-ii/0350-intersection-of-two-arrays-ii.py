class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        shorter, longer = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        counter = Counter(shorter)

        for num in longer:
            print(num, counter)
            if counter[num] > 0:
                counter[num] -= 1
                result.append(num)
        
        return result