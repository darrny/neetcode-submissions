class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet = defaultdict(int)

        for c in s:
            alphabet[c] += 1

        for c in t:
            alphabet[c] -= 1

        for c in alphabet.keys():
            if alphabet[c] != 0:
                return False

        return True