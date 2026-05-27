class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        n = len(digits)
        for i in range(n - 1, -1, -1):
            total = digits[i] + carry
            if total == 10:
                carry = 1
                digits[i] = 0
            else:
                carry = 0
                digits[i] = total

        if carry == 1:
            res = [0] * (n + 1)
            res[0] = 1
            for i in range(n):
                res[i + 1] = digits[i]
            return res

        return digits