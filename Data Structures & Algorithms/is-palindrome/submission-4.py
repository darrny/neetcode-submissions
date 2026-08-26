class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [c.lower() for c in s if c.isalnum()]
        start, end = 0, len(filtered) - 1
        while start <= end:
            if filtered[start] != filtered[end]:
                return False
            start += 1
            end -= 1
        return True