# // O(N)
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         calcedNum = int(''.join(map(str, digits))) + 1
#         return [int(digit) for digit in str(calcedNum)]
# //
# var plusOne = function(digits) {
#     for (let i = digits.length - 1; i >= 0; i--) {
#         if (digits[i] < 9) {
#             digits[i]++;
#             return digits;
#         }
#         digits[i] = 0;
#     }
#     digits.unshift(1);
#     return digits;
# };
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits.insert(0, 1)
        return digits
        