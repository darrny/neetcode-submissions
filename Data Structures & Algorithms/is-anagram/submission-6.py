class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = defaultdict(int)
        for c in s:
            mp[c] += 1
        for c in t:
            mp[c] -= 1
        for c in mp.keys():
            if mp[c] != 0:
                return False
        return True