'''
# 56. Merge Intervals

interval problem. 

1. sorting the intervals by starting time.
2. iterate the intervals array.
    - if the prev end time is bigger than curr start time, it is overlaped.
    solution 1. make a result array.
    solution 2. adjust intervals in-place.
3. return the merged result.
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])

        result = []
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result