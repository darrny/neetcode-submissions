class Solution:
    def longestPalindrome(self, s: str) -> str:
        mx = 0
        best = (0, 0)

        for centre in range(len(s)):
            start, end = centre, centre
            while start >= 0 and end < len(s):
                if s[start] == s[end]:
                    if end - start + 1 > mx:
                        mx = end - start + 1
                        best = (start, end)
                    start -= 1
                    end += 1
                else:
                    break

        for centre in range(len(s)):
            start, end = centre, centre + 1
            while start >= 0 and end < len(s):
                if s[start] == s[end]:
                    if end - start + 1 > mx:
                        mx = end - start + 1
                        best = (start, end)
                    start -= 1
                    end += 1
                else:
                    break
        
        return s[best[0] : best[1] + 1]