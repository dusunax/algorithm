class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True

        s = s.lower()
        converted_s = ''.join(c for c in s if c.isalnum())

        return converted_s == converted_s[::-1]