class Solution:
    # A. String concatenation & Shorter str.
    # idea was => find out the shorter str first, so I can reduce the iteraction count for better TC.
    def mergeAlternatelyA(self, word1: str, word2: str) -> str:
        isWord1Smaller = len(word1) < len(word2)
        result = ""

        # keep word1 is smaller
        if not isWord1Smaller:
            word1, word2 = word2, word1

        while (word1):
            word1First, word1 = word1[0], word1[1:]
            word2First, word2 = word2[0], word2[1:]
            if isWord1Smaller:
                result += word1First + word2First
            else:
                result += word2First + word1First

        if word2:
            result += word2
        
        return result

    # B. Refactored answer
    # - iterate pair using zip(), simplify the code.
    # - list appending is faster than stirng concatenation. 
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []

        for c1, c2 in zip(word1, word2):
            result.append(c1)
            result.append(c2)

        result.append(word1[len(word2):] if len(word1) > len(word2) else word2[len(word1):])

        return "".join(result)