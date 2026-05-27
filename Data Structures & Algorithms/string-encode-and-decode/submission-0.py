class Solution:

    def encode(self, strs: List[str]) -> str:
        ss = ''
        for s in strs:
            length = len(s)
            ss = ss + str(length)
            ss = ss + '#'
            ss = ss + s
        return ss

    def decode(self, s):
        decoded = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            decoded.append(s[j+1:j+1+length])
            i = j + 1 + length
        return decoded