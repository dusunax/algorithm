# return the k amount of element's array
# frequencies = [{1: 3}, {2: 2}, {3: 1}]
# return frequencies.slice(0, k)
# 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = Counter(nums)
        sorted_frequencies = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)
        result = []

        for e in sorted_frequencies:
            result.append(e[0])

        return result[0:k]