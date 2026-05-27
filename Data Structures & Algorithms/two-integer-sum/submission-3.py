class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        n = len(nums)

        for i in range(n):
            curr = nums[i]
            currTarget = target - curr
            
            if currTarget in targets.keys():
                return [targets[currTarget], i]

            targets[curr] = i