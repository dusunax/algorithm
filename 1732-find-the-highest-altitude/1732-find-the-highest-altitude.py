'''
## constaints
- biker point to point.
- start at point 0, altitude 0.
- gain array indicates the altitude movement of bike
- Return the highest altitude reached.

## apporach
- iterate through gain array and accumulate altitude.
- keep track of the maximum altitude.

## pseudocode
highest = 0
altitude = 0

for every gain el
    altitude = altitude + current gain
    highest = max(highest, altitude)
    
return highest
'''
class Solution:
    '''
    TC: O(n)
    SC: O(1)
    '''
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        altitude = 0

        for current in gain:
            altitude += current
            highest = max(highest, altitude)
            
        return highest
