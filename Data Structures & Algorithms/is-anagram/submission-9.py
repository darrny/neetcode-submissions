class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        for c in t:
            counts[c] -= 1
        for c in counts:
            if counts[c] != 0:
                return False
        return True
