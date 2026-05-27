class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []

        for i in range(len(temperatures)):
            res.append(0)

            currTemp = temperatures[i]
            while stack and currTemp > stack[-1][0]:
                poppedTemp, poppedIndex = stack.pop()
                res[poppedIndex] = i - poppedIndex

            stack.append((currTemp, i))

        return res