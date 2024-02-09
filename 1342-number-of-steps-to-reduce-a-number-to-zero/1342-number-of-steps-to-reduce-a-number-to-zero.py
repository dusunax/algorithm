
# ----------------------------
# Javascript
# ----------------------------



# ----------------------------
# Python3
# ----------------------------

# A. modulo
# class Solution:
#     def numberOfSteps(self, num: int) -> int:
#         step = 0

#         while num:
#             if num % 2:
#                 num -= 1
#             else:
#                 num //= 2
#             step += 1

#         return step

# B. bitwise operations
class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0

        while num:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            step += 1

        return step
