class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = []
        max_count = 0

        for char in s:
            if char not in substrings:
                substrings.append(char)
            else:
                max_count = max(max_count, len(substrings))
                substrings = [char]

        return max(max_count, len(substrings))
                