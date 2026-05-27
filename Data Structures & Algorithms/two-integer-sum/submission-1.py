class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        found = {}
        n = len(nums)

        for i in range(n):
            curr = target - nums[i]
            if nums[i] in found.keys():
                return [found.get(nums[i]), i]
            
            found[curr] = i