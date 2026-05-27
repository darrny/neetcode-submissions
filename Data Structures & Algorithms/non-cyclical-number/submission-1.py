class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            total = 0
            while n:
                lastDigit = n % 10
                total += lastDigit * lastDigit
                n = n // 10
            return total

        slow, fast = n, sumOfSquares(n)
        while slow != fast:
            fast = sumOfSquares(fast)
            fast = sumOfSquares(fast)
            slow = sumOfSquares(slow)

        if fast == 1:
            return True
        return False