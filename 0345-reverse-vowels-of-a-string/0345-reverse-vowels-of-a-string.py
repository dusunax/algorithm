'''
vowels revserving 
- a, e, i, o, u
- upper & lower cases: swtich them without convert the case? <- yes

topic hint:
- two pointers

key points
- move the pointers when they are not vowels.
- if you find two vowels? swap them.
- you should consider the case of the char
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        word = list(s)

        while left < right:
            while left < right and self.isVowels(s, left):
                left += 1

            while left < right and self.isVowels(s, right):
                right -= 1

            word[left], word[right] = word[right], word[left]

            left += 1
            right -= 1

        return "".join(word)
        
    def isVowels(self, s: str, i: int) -> bool:
        vowels = {"a", "e", "i", "o", "u"}
        return not s[i].lower() in vowels
