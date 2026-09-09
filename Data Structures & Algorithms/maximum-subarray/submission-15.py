class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = None
        current_sum = 0

        for num in nums:
            current_sum += num

            if maximum is None:
                maximum = current_sum
            else:
                maximum = max(maximum, current_sum)

            if current_sum < 0:
                current_sum = 0

        return maximum