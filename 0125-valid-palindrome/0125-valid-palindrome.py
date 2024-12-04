class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is " ":
            return True

        reg = "[^a-z0-9]"
        converted_s = re.sub(reg, "", s.lower())

        return converted_s == converted_s[::-1]
