class Solution:
    def maxArea(self, height: List[int]) -> int:


        # overview
        # get maximum & second maximum height from height array
        # contain = second maximum * space between two indices 
        # height's integers are not unique value.

        # \U0001f4a1
        # use two pointer indeed, but no need to store the actual values at all, 
        # cuz we got indices for ref the values.

        # \U0001f4a1
        # and "left", "right" naming is quiet common in two pointer solution => might as well use it
        # we can say that's kind of convention for variables name 

        # \U0001f4a1
        # we do not want to find the pointers of maximum & second maximum height
        # we want to find that gets maximum contains
        
        # when do we move the pointers?
        # move the shorter line inward, until the pointers meet
        # left += 1 at height[left] < height[right]
        # right -= 1 at else

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            distance = right - left
            current_area = min(height[left], height[right]) * distance
            max_area = max(current_area, max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
