class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        given = 0

        for num in nums:
            given = given ^ num

        for i in range(n + 1):
            given = given ^ i

        return given