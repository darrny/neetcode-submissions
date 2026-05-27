class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = ''.join(filter(str.isalnum, s))
        print(alphanum)
        lower = alphanum.lower()
        print(lower)
        n = len(lower)

        for i in range(n):
            if lower[i] != lower[n - 1- i]:
                return False

        return True