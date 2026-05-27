class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            m = l + (r - l) // 2

            if nums[m] > target:
                r = m
            elif nums[m] <= target:
                l = m + 1

        if nums[l - 1] == target:
            return l - 1
        else:
            return -1