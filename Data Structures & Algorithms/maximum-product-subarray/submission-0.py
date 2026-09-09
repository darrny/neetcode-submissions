class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mn = [0] * len(nums)
        mx = [0] * len(nums)
        mn[0] = mx[0] = nums[0]

        for i in range(1, len(nums)):
            mx[i] = max(mx[i - 1] * nums[i], mn[i - 1] * nums[i], nums[i])
            mn[i] = min(mx[i - 1] * nums[i], mn[i - 1] * nums[i], nums[i])

        return max(
            max(mn),
            max(mx),
        )