'''
## constaints
- biker point to point.
- start at point 0, altitude 0.
- gain array indicates the altitude movement of bike
- return the highest altitude of a point.

## apporach
- get the each altitudes with gain array.
- keep the highest altitudes.

## sudo
highest = 0
altitude = 0

for every gain el
    altitude = altitude + current gain
    highest = max(highest, altitude)
    
return highest
'''
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        altitude = 0

        for current in gain:
            altitude += current
            highest = max(highest, altitude)
            
        return highest
