class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = Counter(s)

        for i, char in enumerate(s):
            if frequency[char] == 1:
                return i
        
        return -1