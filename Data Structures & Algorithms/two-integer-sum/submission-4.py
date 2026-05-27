class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}

        for i in range(n):
            curr = nums[i]
            currTarget = target - curr

            if currTarget in seen:
                return [seen[currTarget], i]
            
            seen[curr] = i