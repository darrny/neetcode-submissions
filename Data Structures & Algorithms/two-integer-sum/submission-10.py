class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}

        for i, num in enumerate(nums):
            if num in targets:
                return [targets[num], i]
            else:
                targets[target - num] = i
