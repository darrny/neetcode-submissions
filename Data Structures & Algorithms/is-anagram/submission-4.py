class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1
        for c in t:
            cnt[c] -= 1
        for c in cnt.keys():
            if cnt[c] != 0:
                return False
        return True