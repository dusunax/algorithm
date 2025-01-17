class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        
        for num in nums:
            pos = self.bisectLeft(sub, num)
            if pos == len(sub):
                sub.append(num)
            else:
                sub[pos] = num
        
        return len(sub)

    # <bisect.bisect_left> = TC: O(log n)
    # finding the leftmost position in a sorted list
    # where a given target value should be inserted to maintain the list's sorted order
    def bisectLeft(self, list, target) -> int:
        low = 0
        high = len(list) - 1

        while low <= high :
            mid = int(low + (high - low) / 2) 

            print()

            if list[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low
