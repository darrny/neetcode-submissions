class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        res = [float("-inf")] * n
        if n == 1:
            return nums[0]
        arr1 = nums[1::]
        arr2 = nums[0:n-1]

        def helper(arr):
            if not arr:
                return 0
            if len(arr) == 1:
                return arr[0]
            length = len(arr)
            res = [0] * length

            res[0] = arr[0]
            res[1] = max(res[0], arr[1])

            for i in range(2, length):
                res[i] = max(res[i - 1], arr[i] + res[i - 2])

            return max(res[length - 1], res[length - 2])

        return max(helper(arr1), helper(arr2))
