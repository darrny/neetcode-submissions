class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
        for c in t:
            counter[c] -= 1
        for c in counter:
            if counter[c] != 0:
                return False
        return True