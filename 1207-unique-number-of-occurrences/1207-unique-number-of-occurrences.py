'''
- return Is array's elements occurences are unique ? true : false
- can use python class: Counter

1. check frequncey of elements in arr, save to variable
2. check that each frequency value is unique

- unpackin in the for statement has the advantage of avoiding one lookup per value
'''
class Solution:
    '''
    TC: O(n)
    SC: O(n)
    '''
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr) # O(k) => k can be n in worst case
        unique_check = set() # O(k) => same here

        for key, val in freq.items(): # TC: O(n)
            if val in unique_check: # TC: O(1)
                return False
            
            unique_check.add(val) # TC: O(1)

        return True
            
        
        