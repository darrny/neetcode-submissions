class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        numSet = set(nums) # creates a set with the elements in nums
        res = 1

        for num in numSet:
            length = 1
            if (num - 1) not in numSet:
                while (num + length) in numSet:
                    length += 1
                res = max(res, length)

        return res