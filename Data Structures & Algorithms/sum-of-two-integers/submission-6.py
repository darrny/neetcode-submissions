class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0

        for i in range(32):
            aa = (a >> i) & 1
            bb = (b >> i) & 1
            cur_bit = aa ^ bb ^ carry
            carry = (aa + bb + carry) >= 2

            if cur_bit:
                res |= (1 << i)

        if res > 0x7fffffff:
            res = -(res ^ 0xffffffff) - 1
            
        return res