class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency = Counter(s)

        for char in t:
            if char not in frequency or frequency[char] == 0:
                return False
            frequency[char] -= 1

        return True