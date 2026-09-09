class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        srt = sorted(nums)
        seen = set()
        res = []

        for i in range(len(nums)):
            start, end = i + 1, len(nums) - 1
            while start < end:
                if srt[start] + srt[end] + srt[i] == 0:
                    if (srt[i], srt[start], srt[end]) not in seen:
                        seen.add((srt[i], srt[start], srt[end]))
                        res.append([srt[i], srt[start], srt[end]])
                    start += 1
                    end -= 1
                elif srt[start] + srt[end] + srt[i] < 0:
                    start += 1
                else:
                    end -= 1

        return res