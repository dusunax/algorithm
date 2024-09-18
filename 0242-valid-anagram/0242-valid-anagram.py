class Solution:
    # <Use collections.Counter>
    # Time complexity: O(N) + O(N) = O(N)
    # - O(N) for Counter creation, O(N) for comparison
    # Space complexity
    # - Counter for s: O(N)
    
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return Counter(s) == Counter(t) 

    # Manual frequency check
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        frequency = Counter(s)

        for char in t:
            if frequency[char] == 0 or char not in frequency:
                return False
            frequency[char] -= 1
        
        return True