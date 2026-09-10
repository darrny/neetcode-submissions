class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = 0
        mx = 0
        start = 0
        seen = set()

        for end in range(0, len(s)):
            while s[end] in seen:
                seen.remove(s[start])
                curr -= 1
                start += 1

            seen.add(s[end])
            curr += 1
            mx = max(mx, curr)



        return mx