'''
# 2 pointer
TC: O(n)
SC: O(1)
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        max_area = 0

        # proceed until l met r
        while l < r:
            # update max_area
            w = r - l
            h = min(height[l], height[r]) 
            current_area = h * w
            max_area = max(current_area, max_area)

            # find short one, move the pointer
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            
        return max_area

'''            
# \U0001f4a1 Q&A

## 1. Why move shorter pointer. 
- Q. why do we move the *shorter* pointer inward?
- A. the water level is limited by the shoter wall.
    - we are *eliminate* the incorrect or irrelevant options in each steps, and moving taller pointer inward is incorrect move.
    - if we keep the shorter wall and move taller pointer inward, width will decreases *while the limiting height stays the same or goes down*. so the max area of water (min(l, r) * width) can't improve.

## 2. Can we stop moving pointers early?
- Q. can't we stop early when the current max_area is smaller than previous max_area?
- A. \U0001f645‍♀️ if we stop the working through the array early, we possibly missing the chance of way taller walls is exist in the *unknown inward*. so, we have to go through the whole array for checking all possible max_area. and it's O(n).
'''