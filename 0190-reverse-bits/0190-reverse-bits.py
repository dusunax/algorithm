
class Solution:
    # def reverseBitsA(self, n: int) -> int:
    #     bit = bin(n)[2:].zfill(32)
    #     return int(bit[::-1], 2)
  
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1) # shift the result to the left & add LSB of n
            n >>= 1 # shift n to the right & remove previous LSB
        return result