class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = ''.join([c.lower() for c in s if c.isalnum()])
        return stripped == stripped[::-1]