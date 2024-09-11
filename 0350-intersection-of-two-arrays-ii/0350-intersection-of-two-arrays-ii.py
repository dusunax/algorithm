class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        counter = Counter(nums1) # Counter는 요소의 빈도를 세는 데 최적화된 딕셔너리 서브클래스입니다.

        for num in nums2:
            print(num, counter)
            if counter[num] > 0:
                counter[num] -= 1
                result.append(num)
        
        return result