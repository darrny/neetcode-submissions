class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        curr = set()
        n = len(s)
        l = 0
        r = 0
        ret = 0

        while r < n:
            while s[r] in curr:
                curr.remove(s[l])
                l += 1
            curr.add(s[r])
            ret = max(ret, r - l + 1)
            r += 1


        return ret