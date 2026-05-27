class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            total = 0
            while n:
                lastDigit = n % 10
                total += lastDigit * lastDigit
                n = n // 10
            return total

        seen = set()

        while n not in seen:
            seen.add(n)
            n = sumOfSquares(n)
            if n == 1:
                return True
        return False