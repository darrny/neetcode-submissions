class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums)

        for i in range(n):
            curr = nums[i]
            
            if curr in seen.keys():
                return [seen.get(curr), i]

            currTarget = target - curr
            seen[currTarget] = i