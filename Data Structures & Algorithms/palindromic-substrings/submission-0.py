class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for center in range(len(s)):
            start = end = center
            while start >= 0 and end < len(s):
                if s[start] == s[end]:
                    count += 1
                    start -= 1
                    end += 1
                else:
                    break

        for center in range(len(s)):
            start, end = center, center + 1
            while start >= 0 and end < len(s):
                if s[start] == s[end]:
                    count += 1
                    start -= 1
                    end += 1
                else:
                    break

        return count
