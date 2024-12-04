class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True

        converted_s = ''.join(c for c in s.lower() if c.isalnum())

        return converted_s == converted_s[::-1]