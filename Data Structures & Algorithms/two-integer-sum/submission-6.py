class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {} # maps target number : index
        for i, num in enumerate(nums):
            if num in targets:
                return [targets[num], i]
            targets[target - num] = i
    