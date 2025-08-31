# make the `intervals` => non-overlapping 
# find out min number of intervals to remove

# approach
# - sort the array by start.
# - removal_count for return. 
# - iterate: save the ealier `end` of overlapping intervals. count up removal_count when we found the curr interval's `start` is not bigger than prev saved `end`. 

# TC would be O(n), and SC is O(1)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_end = intervals[0][1]
        removal_count = 0

        for [start, end] in intervals[1:]:
            print(start, end)
            if start < prev_end:
               prev_end = min(end, prev_end)
               removal_count += 1
            else:
                prev_end = end

        print(intervals)
        return removal_count