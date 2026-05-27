class Solution:
    def findMin(self, nums: List[int]) -> int:
        target = nums[-1]   # find the last element
        
        l = 0
        r = len(nums) - 1
        ans = -1

        while l <= r:
            m = (l + r) // 2
            if nums[m] <= target:
                ans = m
                r = m - 1
            else:
                l = m + 1

        return nums[ans]