'''
# 57. Insert Interval
- intervals is sorted in ascending order by (start_i)
    - find the correct position using **binary search.**
- insert newInterval, but intervals must not have any overlapping intervals.
    - if they overlap, merge them. <- do not.
- make a new array is recommended?

## do
- use python's bisect_left method.
- insert first, merging later.

## TC & SC
- TC: O(n)
- SC: O(n)
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start_idx = bisect_left([interval[0] for interval in intervals], newInterval[0]) # TC: O(log n)
        
        intervals.insert(start_idx, newInterval) # TC: O(n)

        result = []  # SC: O(n)
        for interval in intervals: # TC: O(n)
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
            
        return result