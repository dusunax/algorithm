# 2 pointer
# move the shorter pointer inward
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
            
        

            
        