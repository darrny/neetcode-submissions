class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current = len(nums) - 1
        required = 0

        while current > 0:
            current -= 1
            required += 1
            if nums[current] >= required:
                required = 0
        
        return required == 0