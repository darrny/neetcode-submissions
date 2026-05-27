class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        res = [float("-inf")] * n

        for i in range(min(n, 2)):
            res[i] = nums[i]

        def dfs(i):
            if i < 0:
                return 0
            if res[i] > float("-inf"):
                return res[i]

            res[i] = max(nums[i] + dfs(i - 2), nums[i] + dfs(i - 3))
            return res[i]
        
        return max(dfs(n - 1), dfs(n - 2))