class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1

        target = 0
        for i in range(n):
            target ^= i
        
        for number in nums:
            target ^= number

        return target