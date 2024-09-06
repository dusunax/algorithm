# // O(N)
# // var plusOne = function(digits) {
# //     const calcedNum = BigInt(digits.join("")) + BigInt(1);
# //     return calcedNum.toString().split("")
# // };
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        calcedNum = int(''.join(map(str, digits))) + 1
        return [int(digit) for digit in str(calcedNum)]
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
        