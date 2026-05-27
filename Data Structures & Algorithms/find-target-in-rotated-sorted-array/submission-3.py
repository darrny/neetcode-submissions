class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rot = -1
        t = nums[-1]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] <= t:
                rot = m
                r = m - 1
            else:
                l = m + 1
        
        if t == target:
            return len(nums) - 1
        elif t < target:
            l, r = 0, rot - 1
        else:
            l, r = rot, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1