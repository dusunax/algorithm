class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        sign = 1
        index = 0
        max = 2 ** 31 - 1
        min = -(2 ** 31)
        
        # step 1
        s = s.strip()
        if s == "":
            return 0

        # step 2
        if s[index] == "-":
            sign = -1
            index += 1
        elif s[index] == "+":
            index += 1

        # step 3
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1

            if sign * result > max:
                return max
            elif sign * result < min:
                return min

        return result * sign

        