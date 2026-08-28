class Solution:
    def reverseBits(self, n: int) -> int:
        target = 0

        for i in range(32):
            if n & 1:
                target |= 1
            n >>= 1
            
            if i == 31:
                return target

            target <<= 1
