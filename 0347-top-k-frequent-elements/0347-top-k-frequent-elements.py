# return the k amount of element's array
# frequencies = [{1: 3}, {2: 2}, {3: 1}]
# return frequencies.slice(0, k)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]

        for num, freq in frequency_map.items():
            buckets[freq].append(num)

        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
