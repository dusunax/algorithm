'''
# 435. Non-overlapping Intervals

- 인터벌이 오버래핑 되지 않기위해 지워야하는 인터벌의 최소값 반환
- 그래프에 순환이 있는지 여부를 알아본다 <- ❌ overkill
- should approach with => Greedy 

## Greedy
- if you detecte interval overapping, you should remove
    - not physically. keeping counts is enough.
- Todo: keep many intervals, so can minimize removal as possible.

## how to detects overlaps?
- sorts intervals by ends, iterate intervals with tracking down the prev_end
- current_start < prev_end
    - if start time is smaller than a prev_end = overlap 
        - ex) [2, 4] is overlap with [1, 3]
            - start (2) is smaller than end (3)
    - keep the interval ends first

## which one should removed?
- when overlap, what to remove comparson is => one's ends later (because it restricts more future intervals).
    - leave the most room for the future non-overlapping intervals.
    - the longer an interval lasts, the more it blocks others.

## how to perform
- sorts interval as ends
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        count = 0 # don't need to trackdown everything
        prev_end = intervals[0][1] # tracking the last end time
        
        for start, end in intervals[1:]: # 1 ~ n-1
            if start < prev_end: # overlap detection
                count += 1 
                # not moving the prev_end pointer == prev_end is still pointing at the previous interval  == keeping the interval ends earlier
            else: 
                prev_end = end
        
        return count

        
        