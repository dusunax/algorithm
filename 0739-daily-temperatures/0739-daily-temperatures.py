'''
# what is monotonic stack?

- hum..
                  72
              69  69  72  76
  74  75  71  71  71  71  72  76      73
  73  74  75  75  75  75  75  75  76  76
  ⁝    ⁝           ⁝    ⁝   ⁝    ⁝   ⁝   ⁝
  1    1          1   2   1   4   0   0

- save the pop count in each indices
    => no need to keep tracking the counts of the each pops. => keeps indices.
    => and use T as a stack. No need to build a new one.
- pop count is indices's distance.

=> use this [73, 74, 75, 71, 69, 72, 76, 73] and keep indices. [0,1,2,3,4,5]

Iterate T
- start at 1, T[0] 73 is smaller than T[1] 74. 
  => pop 73, and T[0] is 1 - 0 = 1
- next is 2, T[1] 74 is smaller than T[2] 75. 
  => pop 74, and T[1] is 2 - 1 = 1
- next is 3, T[2] 75 is not smaller than T[3] 71.
  => ? 

- pop the last => compare with top of the stack.
- keep indices, not values. compute the distance `i - prev`
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]: # stack is not empty, T[i] > T[stack[-1]] => T[i] is bigger than last element
                prev = stack.pop()
                result[prev] = i - prev # paste it.
            stack.append(i) # keep it for next iteration

        return result