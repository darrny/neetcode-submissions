class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        res = []

        for word in strs:
            key = tuple(sorted(word))
            groups[key].append(word)

        for group in groups.values():
            res.append(group)

        return res