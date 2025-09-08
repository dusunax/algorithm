'''
# Problem
- find *.
- remove left non-* and * 
- return result.

## Key point
- The problem is always possible.
  - very left char is always non-*
  - * has always matching non-*

## Stack
- Start at very left element.
- put into the stack and remove the * and before(left) element when you find *
- if you find *? don't bother to put it in and pop it. just remove last element.

## TC & SC
- TC is O(n)
  - Iterate array once = O(n), Stack operation (push/pop operate only at the end) = O(1)
- SC is O(n)
  - Keep a stack for hold every element at once(at least non-star ones) = O(n)
'''
class Solution:
    '''
    # Stack
    - TC: O(n)
    - SC: O(n)
    '''
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack) 
        