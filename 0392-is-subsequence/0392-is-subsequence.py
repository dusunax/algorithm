'''
## constraint
- given two strings: s, t
- they are lowercases.
- return bool of if s is subsequence of t
- s is much smaller than t: s is up to 100, t is up to 10^4

## approach
- ❌ get the frequencies, compares them => x. need to compare "stable" way.
- ❌ if iterate s, and find out each char is vaild by iterate t? => SC will be O(n^2)
- ✅ two pointer: use pointer for s & t

## sudo
```
s_pointer = 0
t_pointer = 0

while s_pointer is smaller than s.lengh, and t_pointer is smaller than t.length
    check if t pointer and s pointer matches.
        move s_pointer +=1 (found a match, move to next char in s)
    move t_pointer +=1 (always forward in t)
    
    if s_pointer's pointer is same as s.len return true.
    else return false
```
- \U0001f4cc we are moving pointers, we can check the valid with where they pointed in the end.
''' 

class Solution:
    '''
    TC: O(n)
    SC: O(1)
    '''
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        t_pointer = 0

        while s_pointer < len(s) and t_pointer < len(t): # O(len(t))
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            t_pointer += 1

        return s_pointer == len(s)


        