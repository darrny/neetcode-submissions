class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
            
        maxReachable = 0
        maxInWindow = 0
        steps = 0
        target = len(nums) - 1

        for i in range(len(nums)):
            if i + nums[i] > maxReachable:
                maxReachable = i + nums[i]
            if i == maxInWindow:
                steps += 1
                maxInWindow = maxReachable
                if maxInWindow >= target:
                    return steps