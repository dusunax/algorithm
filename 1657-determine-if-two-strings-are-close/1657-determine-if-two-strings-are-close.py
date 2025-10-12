'''
# isClose Ops
- Op1. swap 2 exisiting characters
- Op2. every char into another char

# approach
- op1 can proceed as many times as needed, so char's order is irrelavent. use set to compare.
- use Frequncey Counter (python)

# Set / Map
- `Set` for compare two string
- `Map` for count chars (+ multiset)
'''
class Solution:
    '''
    TC: O(n)
    => py sorting op is `nlogn`, but, sorting(k) at most 26 numbers => constant O(1).
    => so it is O(n)
    SC: O(n)
    '''
    def closeStrings(self, word1: str, word2: str) -> bool:
        # set: alphabet compare
        s1 = set(word1) # TC: O(n)
        s2 = set(word2) # same
        if s1 != s2:
            return False

        # map
        c1 = Counter(word1) # TC: O(n)
        c2 = Counter(word2)
        return True if sorted(c1.values()) == sorted(c2.values()) else False
        
        # c1_multiset = []
        # c2_multiset = []
        # for _char, count in c1.items():
        #     c1_multiset.append(count)
        # for _char, count in c2.items():
        #     c2_multiset.append(count)

        # c1_multiset.sort()
        # c2_multiset.sort()

        # return True if c1_multiset == c2_multiset else False