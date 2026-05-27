class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = defaultdict(int)
        sum = 0
        n = len(nums)
        def dfs(index, currSum, target, nums):
            if (index, currSum) in cache:
                return cache[(index, currSum)]
            if index == n and currSum == target:
                return 1
            if index == n:
                return 0

            positive = dfs(index + 1, currSum + nums[index], target, nums)
            negative = dfs(index + 1, currSum - nums[index], target, nums)
            cache[(index, currSum)] = positive + negative
            return positive + negative
        return dfs(0, 0, target, nums)