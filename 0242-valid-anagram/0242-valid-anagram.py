class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        frequency = Counter(s)

        for char in t:
            if frequency[char] == 0 or char not in frequency:
                return False
            frequency[char] -= 1
        
        return True