class Solution:
    def reverseBits(self, n: int) -> int:
        bit = bin(n)[2:].zfill(32)
        return int(bit[::-1], 2)

        # result = 0
        # for i in range(32):
        #     result = (result << 1) | (n & 1)
        #     n >>= 1
        # return result