class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_letters = {}

        for char in magazine:
            magazine_letters[char] = magazine_letters.get(char, 0) + 1
            # get(char, 기본값) ~> char 키가 존재하지 않으면 기본값을 반환한다.

        for char in ransomNote:
            if char not in magazine_letters or magazine_letters[char] == 0:
                return False
            
            magazine_letters[char] -= 1
        
        return True