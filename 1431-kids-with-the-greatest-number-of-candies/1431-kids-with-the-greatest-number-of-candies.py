class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candie = max(candies)
        is_grested_candie_list = [(True if e + extraCandies >= max_candie else False) for e in candies]
        return is_grested_candie_list
        
'''
- extraCandies = extra candies that I have.
- after giving them candies
    - true: they will have the greatest number of candies
    - false: otherwise.

## approach.
- find out greatest number, max_candie.
- iterate should be just once, check if current + extraCandies is bigger than max_candie.

## note
- n is bigger or equal than 2, smaller or equal than 100. => no need for exception of that.
- max length of candies is 100, and extraCandies is 50. => there will be no significant performance issues.
- there could be multiple greatest candies. => so it should be `e + extraCandies >= max_candie`, not `>`
'''