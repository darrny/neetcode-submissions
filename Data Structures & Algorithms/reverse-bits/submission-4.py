class Solution:
    def reverseBits(self, n: int) -> int:
        target = 0

        for _ in range(31):
            if n & 1:
                target |= 1
            target <<= 1
            n >>= 1

        if n & 1:
            target |= 1   
        return target