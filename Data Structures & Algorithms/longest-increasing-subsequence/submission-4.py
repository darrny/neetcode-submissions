class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        dp[-1] = 1

        for i in range(len(nums) - 2, - 1, -1):
            mx = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    mx = max(mx, dp[j] + 1)

            dp[i] = mx

        print(dp)
        return max(dp)