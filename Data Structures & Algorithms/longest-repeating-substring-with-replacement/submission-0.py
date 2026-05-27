class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            correctCount = 0
            wrongCount = 0
            l = 0

            for r in range(len(s)):
                if s[r] == c:
                    correctCount += 1
                else:
                    wrongCount += 1

                while wrongCount > k:
                    if s[l] == c:
                        correctCount -= 1
                        l += 1
                    else:
                        wrongCount -= 1
                        l += 1
                res = max(r - l + 1, res)

        return res