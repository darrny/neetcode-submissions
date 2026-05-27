class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        fwd = [1] * n
        bwd = [1] * n

        curr = 1
        for i in range(n):
            curr *= nums[i]
            fwd[i] = curr

        curr = 1
        for i in range(n - 1, 0, -1):
            curr *= nums[i]
            bwd[i] = curr

        if n == 2:
            return [nums[1], nums[0]]

        res = [1] * n
        res[0] = bwd[1]
        res[n - 1] = fwd[n - 2]

        for i in range(1, n - 1, 1):
            res[i] = fwd[i - 1] * bwd[i + 1]

        return res