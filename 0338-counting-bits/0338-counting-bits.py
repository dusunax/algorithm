class Solution:
    '''
    brute force
    '''
    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(int(n) + 1):
            result.append(bin(i).count('1'))
        
        return result

        
        
        