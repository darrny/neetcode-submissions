class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i in range(len(nums)):
            newTarget = target - nums[i]
            if newTarget in complements:
                return [complements[newTarget], i]
            else:
                complements[nums[i]] = i
        