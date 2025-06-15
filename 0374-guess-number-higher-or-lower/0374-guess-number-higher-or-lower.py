# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

'''
binary search
- higher or lower, guessing number game
- guess(): -1 | 1 | 0
'''

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n

        while low <= high:
            mid = (low + high) // 2

            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                low = mid+1
            else:
                high = mid-1

    # ❌ not it - binary search need low and high bounds
    # def guessNumber(self, n: int) -> int:
    #     current = int(n/2) + 1

    #     for i in range(5):
    #         gussing_result = guess(current)

    #         if gussing_result == 0:
    #             return current
    #         elif gussing_result == 1:
    #             current = int((current + n) / 2)
    #         else:
    #             current = int(current/2)