class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = sorted(word)
            groups[str(key)].append(word)
        res = []
        for key, lst in groups.items():
            res.append(lst)
        return res