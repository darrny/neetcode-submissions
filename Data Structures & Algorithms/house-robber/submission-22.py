class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        house_max = [0] * len(nums)
        house_max[0] = nums[0]
        house_max[1] = max(nums[1], house_max[0])

        for i in range(2, len(nums)):
            house_max[i] = max(house_max[i - 1], house_max[i - 2] + nums[i])

        return house_max[-1]