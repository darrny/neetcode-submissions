class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}

        for i in range(n):
            curr = target - nums[i]
            if curr in seen:
                return [seen[curr], i]
            seen[nums[i]] = i