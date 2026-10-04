class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        res = l = 0

        for r, char in enumerate(s):
            count[ord(char) - ord('A')] += 1
            maxf = max(count)

            while (r - l + 1 - maxf) > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
                maxf = max(count)

            res = max(res, r - l + 1)

        return res
                