class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        print("" in parentheses_map)

        for char in s:
            if char in parentheses_map:
                stack.append(char)
            else:
                if len(stack) == 0 or parentheses_map[stack.pop()] != char:
                    return False
        
        return not stack


        
        
        
        
